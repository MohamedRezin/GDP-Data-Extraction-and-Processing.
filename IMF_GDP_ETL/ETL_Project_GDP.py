import pandas as pd
import sqlite3
from datetime import datetime

# File Path

html_file = "Data/GDP.html"
json_path = "Data/Countries_by_GDP.json"
db_name = "Data/World_Economies.db"
table_name = "Countries_by_GDP"
log_file = "logs/ETL_Ptoject_Log.txt"

# Logging Function
def log_progress(message):
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file, "a") as f:
        f.write(timestamp + " : " + message + "\n")


# Extract Function

def extract():
    tables = pd.read_html(html_file)
    df = tables[3]
    return df

#Transform Function

def transform(df):

    df = df[
        [
            ("Country/Territory", "Country/Territory"),
            ("IMF[1][13]", "Estimate")
        ]
    ]

    df.columns = ["Country", "GDP_USD_Billion"]

    df["GDP_USD_Billion"] = (
        pd.to_numeric(
            df["GDP_USD_Billion"]
            .astype(str)
            .str.replace(",", "", regex=False),
            errors="coerce"
        )
        / 1000
    ).round(2)

    df = df.dropna(subset=["GDP_USD_Billion"])

    return df

# Load JSON Function

def load_to_json(df):
    df.to_json(json_path,orient="records")
    
# Load Database Function

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


# Main ETL Workflow 

log_progress("ETL Pipeline Initiated")

log_progress("Extract phase Initiated")
df = extract()
log_progress("Extract phase Completed")

log_progress("Transform phase Initiated")
df = transform(df)
log_progress("Transform phase Completed")

log_progress("JSON Load Initiated")
load_to_json(df)
log_progress("JSON Load Completed")

log_progress("Database Load Initiated")
load_to_db(df)
log_progress("Database Load Completed")

log_progress("Query Execution Initiated")
query = f"""
SELECT *
FROM {table_name}
WHERE GDP_USD_Billion > 100
"""
run_query(query)
log_progress("Query Execution Completed")

log_progress("ETL Process Completed")