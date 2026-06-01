import numpy as np
import pandas as pd

def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# Extraction of the tables from the local HTML file

tables = pd.read_html("GDP.html")

# Retain table number 3 as the required dataframe
df = tables[3]

# Replacement of Column headers with Column Numbers
df.columns = range(df.shape[1])

# Retention of columns with index 0 and 2
# [Name of the Country and Value of GDP quoted by IMF]
df = df[[0, 2]]

# Retention of the Rows with index 1 to 10,
# indicating the top 10 economies of the world.
df = df.iloc[1:11, :]

# Assignment of column names
df.columns = ["Country", "GDP(Million USD)"]

# Change the datatype of GDP Column to Integer using astype() method.
df["GDP(Million USD)"] = df["GDP(Million USD)"].astype(int)

# Conversion of GDP Value in Millions to Billions USD
df[["GDP(Million USD)"]] = df[["GDP(Million USD)"]]/1000

# Round the value to 2 decimal places using numpy.round() function
df[['GDP(Million USD)']] = np.round(df[['GDP(Million USD)']], 2)

# Rename Column
df.rename(columns = {"GDP(Million USD)" : "GDP (Billion USD)"},inplace=True)

# Display the dataframe
print(df)

