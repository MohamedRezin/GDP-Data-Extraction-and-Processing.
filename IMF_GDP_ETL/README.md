# IMF GDP ETL Pipeline

## Overview

This project demonstrates the implementation of a complete ETL (Extract, Transform, Load) pipeline using Python.

The objective is to automate the extraction and processing of country GDP information from a web source and make the data accessible in multiple structured formats for analysis and querying.

The project simulates a real-world data engineering workflow where periodically updated economic data must be collected, processed, stored, and made available for business decision-making.

## Project Scenario

An international organization planning global expansion requires updated GDP information for countries around the world.

As a Junior Data Engineer, the task is to design an automated ETL pipeline that:

- Extracts GDP data from a web source
- Processes and transforms the information
- Stores the results in JSON format
- Loads the processed data into a database
- Executes SQL queries on the stored data
- Maintains execution logs for monitoring and auditing

## Objectives

- Extract GDP data using web scraping
- Transform and clean GDP information
- Round GDP values to two decimal places
- Export data as a JSON file
- Store processed data in an SQLite database
- Query database records
- Log execution progress

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLite
- JSON
- SQL
- Logging

## Workflow

### Extract

Retrieve GDP data from the target web source and extract relevant tabular information.

### Transform

Clean and process GDP values and prepare the dataset for structured storage.

### Load

- Export processed data to JSON
- Load data into SQLite database

### Query

Execute SQL queries to retrieve countries with GDP values exceeding specified thresholds.

### Logging

Maintain execution logs to monitor and document pipeline activity.

## Skills Demonstrated

- ETL Pipeline Development
- Web Scraping
- Data Transformation
- JSON Processing
- SQLite Integration
- SQL Querying
- Logging and Monitoring
- Data Engineering Workflow

## Output

The project generates:

- Countries_by_GDP.json
- World_Economies.db
- etl_project_log.txt

The final database enables efficient querying of countries ranked by GDP.

## Author

Mohamed Rezin  
B.Tech CSE (Big Data Analytics)  
SRM Institute of Science and Technology
