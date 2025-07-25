# Tech Layoffs Analysis (2020-2025)

## 📊 Live Dashboard

**You can view and interact with the live dashboard here:** [**LINK TO YOUR PUBLIC POWER BI REPORT**]

*Paste the public link you got from Power BI Service here.*

---

## About The Project

This project analyzes tech industry layoffs using data compiled by [Layoffs.fyi](https://layoffs.fyi/). The data was processed using Python and visualized in a comprehensive Power BI dashboard to uncover trends related to companies, locations, industries, and funding stages.

### Key Insights & Features
* Total layoffs over time.
* Top companies and industries with the most layoffs.
* Geographical distribution of layoffs by country and city.
* Analysis of layoffs based on company funding stage.

---

## Tech Stack

* **Data Processing:** Python, Pandas
* **Data Storage (for script):** MySQL
* **Data Visualization:** Power BI
* **Data Source:** [Layoffs.fyi](https://layoffs.fyi/)

---

## How to Run This Project Locally

To run the data processing script yourself, follow these steps:

1.  Clone the repository:
    ```sh
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    ```
2.  Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
3.  Set up a local MySQL server and create a database named `layoffs_db`.
4.  **Important:** You will need to add your own MySQL credentials to the Python script to run it.
5.  Run the Python script:
    ```sh
    python data_processing.py
    ```