import pandas as pd 
import numpy as np 
import requests
import bs4
import lxml 
from datetime import datetime
import sqlite3


# Task 1 :  Logging Function

log_file = "banks_project.txt"
def log_progress(message):
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file,"a") as f:
        f.write(timestamp+" : "+message+"\n")


log_progress("Preliminaries complete. Initiating ETL Process")

# Task 2 : Extraction of Data 

def extract():
    html_file = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    tables = pd.read_html(html_file)
    df = tables[1]
    df = df.iloc[:, [1,2]]
    df.columns = ["Name","MC_USD_Billion"]
    df["MC_USD_Billion"] = (
        df["MC_USD_Billion"]
        .astype(str)
        .str[:-1]
        .astype(float)
    )
    return df 
 
log_progress("Data extraction complete. Initiating Transformation process")
df = extract()



# Task 3 : Transformation of Data 
csv_path = "exchange_rate.csv"
def transform(df):
    exchange_rate = pd.read_csv(csv_path,index_col=0).to_dict()["Rate"]

    gbp_rate = float(exchange_rate["GBP"])
    eur_rate = float(exchange_rate["EUR"])
    inr_rate = float(exchange_rate["INR"])

    df["MC_GBP_Billion"] = [
        np.round(x * gbp_rate, 2)
        for x in df["MC_USD_Billion"]
    ]
    df["MC_EUR_Billion"] = [
        np.round(x * eur_rate, 2)
        for x in df["MC_USD_Billion"]
    ]
    df["MC_INR_Billion"] = [
        np.round(x * inr_rate, 2)
        for x in df["MC_USD_Billion"]
    ]
    return df

log_progress("Data Transformation complete. Initiating Loading process")
df = transform(df)

# Task 4 : Loading to CSV 

csv_path = "Banks.csv"
def load_to_csv(df):
    df.to_csv(csv_path)

log_progress("Data saved to CSV file")
load_to_csv(df)

# Task 5 : Loading to Database and Query Call 

db_name = "Banks.db"
table_name = "Largest_banks"

# Load to Database
def load_to_db(df):
    conn = sqlite3.connect(db_name)
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()

# Query Function
def run_query(query_statement):
    conn = sqlite3.connect(db_name)
    query_output = pd.read_sql(query_statement, conn)
    print(query_output)
    conn.close()

log_progress("SQL Connection Initiated")
load_to_db(df)
log_progress("Data loaded to Database as a table, Executing queries")

query1 = """
SELECT *
FROM Largest_banks
"""
run_query(query1)

query2 = """
SELECT AVG(MC_GBP_Billion)
FROM Largest_banks
"""
run_query(query2)

query3 = """
SELECT Name
FROM Largest_banks
LIMIT 5
"""
run_query(query3)

log_progress("Process Complete")
log_progress("Server Connection Closed")

