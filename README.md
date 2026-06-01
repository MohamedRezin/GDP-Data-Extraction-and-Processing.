# GDP Data Extraction and Processing

## Overview

This project demonstrates the process of collecting, processing, and storing economic data using Python. The objective is to extract information about the world's largest economies by Gross Domestic Product (GDP) from a publicly available web source, transform the data into a structured format, and export the results for further analysis.

The project simulates a real-world data engineering task in which a multinational organization requires reliable economic indicators to support strategic expansion decisions.

## Project Scenario

An international company plans to expand its operations across multiple countries and requires economic insights to support its decision-making process.

As a Junior Data Engineer, the task is to create a data pipeline that:

- Extracts GDP data from a web source
- Identifies the top 10 largest economies
- Processes and transforms the information
- Stores the results in a structured CSV format

## Data Source

Archived Wikipedia page containing nominal GDP statistics:

https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29

## Objectives

- Extract data from a website using web scraping techniques
- Process tabular data using Pandas
- Perform data transformations using NumPy
- Identify the top 10 economies by GDP
- Round GDP values to two decimal places
- Export processed results to a CSV file

## Technologies Used

- Python
- Pandas
- NumPy
- Requests
- BeautifulSoup
- CSV

## Workflow

1. Retrieve web page data
2. Extract GDP table information
3. Load data into a Pandas DataFrame
4. Clean and transform GDP values
5. Select the top 10 economies
6. Export processed data to CSV

## Skills Demonstrated

- Data Extraction
- Web Scraping
- HTTP Requests
- Data Cleaning
- Data Transformation
- Data Analysis
- ETL Fundamentals
- CSV Data Processing

## Repository Structure

gdp-data-extraction-processing/
│
├── README.md
├── gdp_extraction.py
├── data/
│   ├── raw_data.csv
│   └── processed_data.csv
│
├── screenshots/
│
└── docs/

## Sample Output

The final output contains the top 10 largest economies ranked by GDP in billions of USD.

## Author

Mohamed Rezin
B.Tech CSE (Big Data Analytics)
SRM Institute of Science and Technology
