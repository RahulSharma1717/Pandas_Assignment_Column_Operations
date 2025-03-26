import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract Year, Month, and Day into separate columns
df["Date_Year"] = df["Date"].dt.year
df["Date_Month"] = df["Date"].dt.month
df["Date_Day"] = df["Date"].dt.day

print(df)