import pandas as pd

# Read Bronze JSON
df = pd.read_json("data/bronze/stock_raw.json")

# Show first few rows
print(df.head())

# Save to Silver
df.to_csv(
    "data/silver/aapl_clean.csv",
    index=False
)

print("Silver file created")