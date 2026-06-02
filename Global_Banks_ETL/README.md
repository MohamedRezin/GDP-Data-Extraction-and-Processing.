# Global Banks ETL Pipeline

## Overview

This project demonstrates the design and implementation of an ETL pipeline for extracting, transforming, and storing financial information related to the world’s largest banks by market capitalization.

The pipeline processes market capitalization data, converts values into multiple currencies, and stores the results in structured formats suitable for analysis and database querying.

The project reflects a practical data engineering workflow supporting multinational business operations.

## Project Scenario

A multinational organization requires financial information regarding the largest banks in the world ranked by market capitalization.

As a Data Engineer, the task is to create a pipeline that:

- Extracts banking data from a web source
- Converts market capitalization values into multiple currencies
- Stores processed information locally
- Loads the transformed dataset into a database
- Executes region-specific business queries
- Logs execution progress

## Objectives

- Extract tabular bank data using web scraping
- Load extracted data into a Pandas DataFrame
- Transform market capitalization values
- Convert values into GBP, EUR, and INR
- Round transformed values to two decimal places
- Export processed data to CSV
- Store transformed data in an SQLite database
- Execute SQL queries for regional offices
- Maintain execution logs

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLite
- CSV
- SQL
- Logging

## Workflow

### Extract

Retrieve market capitalization data for major global banks from the designated web source.

### Transform

Apply exchange rate conversions and generate additional market capitalization columns for:

- USD
- GBP
- EUR
- INR

### Load

- Export transformed data to CSV
- Load processed information into database tables

### Query

Execute SQL queries supporting:

- London Office (GBP)
- Berlin Office (EUR)
- New Delhi Office (INR)

### Logging

Track and document ETL execution using log files.

## Skills Demonstrated

- ETL Pipeline Development
- Financial Data Processing
- Currency Conversion
- CSV Processing
- SQLite Database Management
- SQL Querying
- Logging and Monitoring
- Business-Oriented Data Engineering

## Output

The project generates:

- Processed CSV output
- SQLite database table
- Execution log file

The final solution enables stakeholders from different regions to access financial information in their preferred currency.

## Author

Mohamed Rezin  
B.Tech CSE (Big Data Analytics)  
SRM Institute of Science and Technology
