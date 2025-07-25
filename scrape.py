import pandas as pd
import mysql.connector

# STEP 1: Load CSV
df = pd.read_csv("Layoffs_fyi.csv")

# STEP 2: Clean Columns
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

# Rename if needed
df.rename(columns={
    'location_hq': 'location',
    '#_laid_off': 'laid_off',
    '%': 'percent',
    '$_raised_(mm)': 'raised_million'
}, inplace=True)

# Convert types
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

if 'raised_million' in df.columns:
    df['raised_million'] = df['raised_million'].replace('[\$,]', '', regex=True).astype(float)

# STEP 3: Connect to MySQL Workbench
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',   # <-- use your actual password
    database='layoffs_db'
)
cursor = conn.cursor()

# STEP 4: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tech_layoffs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(255),
    location VARCHAR(255),
    laid_off INT,
    date DATE,
    percent VARCHAR(10),
    industry VARCHAR(255),
    source TEXT,
    stage VARCHAR(100),
    raised_million FLOAT,
    country VARCHAR(100),
    date_added DATE
);
""")
conn.commit()

# STEP 5: Insert Data
for _, row in df.iterrows():
    row = row.where(pd.notnull(row), None)  # ✅ Replace NaNs with None
    
    cursor.execute("""
        INSERT INTO tech_layoffs 
        (company, location, laid_off, date, percent, industry, source, stage, raised_million, country, date_added)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row.get('company'),
        row.get('location'),
        int(row['laid_off']) if row.get('laid_off') is not None else None,
        row['date'].date() if row.get('date') is not None else None,
        row.get('percent'),
        row.get('industry'),
        row.get('source'),
        row.get('stage'),
        row.get('raised_million'),
        row.get('country'),
        row['date_added'].date() if row.get('date_added') is not None else None
    ))

conn.commit()

cursor.close()
conn.close()
print("✅ Data inserted successfully into MySQL!")
