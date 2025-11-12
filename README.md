# 🌞 Solar Data Discovery Challenge - Week 1

This repository contains the complete analysis for the **10 Academy Solar Data Discovery Challenge**.  
The project focuses on analyzing solar farm data from **Benin**, **Sierra Leone**, and **Togo** to provide a **strategic recommendation** for future solar investments by **MoonLight Energy Solutions**.

The work is divided into three technical tasks and one bonus dashboard section — covering environment setup, data cleaning, exploratory data analysis (EDA), cross-country comparison, and visualization.

---

## 📑 Table of Contents
1. [Project Structure](#project-structure)
2. [Setup and Installation](#setup-and-installation)
3. [Task 1: Git & Environment Setup](#task-1-git--environment-setup)
4. [Task 2: Data Profiling, Cleaning & EDA](#task-2-data-profiling-cleaning--eda)
5. [Task 3: Cross-Country Comparison](#task-3-cross-country-comparison)
6. [Bonus Task: Interactive Dashboard with Streamlit](#bonus-task-interactive-dashboard-with-streamlit)
7. [Final Report and Submission](#final-report-and-submission)

---
## Setup and Installation
To set up the project locally and reproduce the analysis, please follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<your-username>/solar-challenge-week1.git
    cd solar-challenge-week1
    ```

2.  **Create and activate a Python virtual environment:**
    A virtual environment is crucial for managing project-specific dependencies.
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate the environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    The `requirements.txt` file contains all the necessary libraries to run the notebooks and the Streamlit app.
    ```bash
    pip install -r requirements.txt
    ```

## Task 1: Git & Environment Setup
This initial task focused on establishing a professional, version-controlled development environment.
*   A **Git repository** was initialized and structured with best practices, including the use of a feature branch (`setup-task`) for initial work.
*   A **`.gitignore`** file was configured to exclude sensitive data, virtual environments, and other non-essential files.
*   A **Continuous Integration (CI) workflow** was set up using GitHub Actions (`.github/workflows/ci.yml`). This workflow automatically verifies that the project dependencies install correctly on a clean Linux environment on every push and pull request, preventing integration issues.

## Task 2: Data Profiling, Cleaning & EDA
This task involved a deep dive into each country's individual dataset to clean, preprocess, and understand its unique characteristics.

*   **Process:** For each country (Benin, Sierra Leone, Togo), a separate Jupyter Notebook was used (e.g., `notebooks/benin_eda.ipynb`).
*   **Cleaning Steps:**
    1.  **Data Loading:** Loaded the raw CSV and set the `Timestamp` as a datetime index.
    2.  **Outlier Removal:** Identified and removed extreme outliers using the Z-score method (where `|Z| > 3`).
    3.  **Missing Value Imputation:** Filled null values in key numerical columns with the column's median.
    4.  **Export:** Saved the processed data as a new file (e.g., `data/benin_clean.csv`).
*   **Analysis:** The notebooks contain detailed exploratory analysis, including time-series plots, correlation heatmaps, and wind rose visualizations.

## Task 3: Cross-Country Comparison
This task synthesized the three cleaned datasets to provide a comparative analysis and answer the core business question.

*   **Process:** The `notebooks/compare_countries.ipynb` notebook loads the three `_clean.csv` files into a single DataFrame.
*   **Analysis Techniques:**
    1.  **Visual Comparison:** Side-by-side boxplots were used to compare the distribution of key metrics like Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI).
    2.  **Statistical Summary:** A summary table was generated to compare the mean, median, and standard deviation of these metrics across the countries.
    3.  **Statistical Testing:** A Kruskal-Wallis H-test was performed to determine if the observed differences in GHI were statistically significant.

## Bonus Task: Interactive Dashboard with Streamlit
To make the findings accessible and interactive, a web dashboard was built using Streamlit.

*   **Location:** The source code for the app is located in the `app/` directory, with `app/main.py` as the main script.
*   **Features:**
    *   An interactive sidebar to filter the data by country.
    *   Dynamic visualizations, including boxplots and bar charts, that update based on user selection.
    *   A clear summary statistics table for quick comparison.
*   **How to Run the Dashboard Locally:**
    1.  Ensure you have completed the "Setup and Installation" steps.
    2.  Run the following command from the project's root directory:
        ```bash
        streamlit run app/main.py
        ```
    3.  Your default web browser will open a new tab with the interactive dashboard.

## Final Report and Submission
The culmination of this project is a final strategic report and the organized repository itself.
*   **Final Report:** A comprehensive summary of the project's methodology, findings, and final recommendation is available in `final_report.pdf`.
*   **Dashboard Screenshot:** A screenshot of the final, functioning Streamlit dashboard can be found in the `dashboard_screenshots/` directory.
## 🗂 Project Structure

The repository is organized for clarity and modular development.

```bash
solar-challenge-week1/
├── .github/               # CI/CD workflows for automated checks
├── app/                   # Streamlit interactive dashboard source code
├── dashboard_screenshots/ # Screenshots of the final dashboard
├── data/                  # Raw and cleaned data files (ignored by .gitignore)
├── notebooks/             # Jupyter Notebooks for EDA and analysis
├── .gitignore             # Files and directories ignored by Git
├── final_report.pdf       # Final summary report in PDF format
├── README.md              # This documentation file
└── requirements.txt       # Python dependencies list



