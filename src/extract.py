'''import yfinance as yf

ticker = "AAPL"

df = yf.download(ticker, period="30d")

print(df.head())

print("\nColumns:")
print(df.columns)


o/p -->

Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date                                                                
2026-08-18  310.029999  311.489990  305.739990  307.579987  53424500
2026-08-19  316.829987  319.279999  309.600006  310.140015  50505600
2026-08-20  311.299988  320.279999  310.649994  317.459991  40959200
2026-08-21  309.350006  312.380005  307.010010  312.049988  46876800
2026-08-24  310.339996  313.359985  309.970001  311.470001  34673600

Columns:
MultiIndex([( 'Close', 'AAPL'),
            (  'High', 'AAPL'),
            (   'Low', 'AAPL'),
            (  'Open', 'AAPL'),
            ('Volume', 'AAPL')],
           names=['Price', 'Ticker'])
(venv) radhikamangroliya@RADHIKAs-MacBo'''

import yfinance as yf
import json
from pathlib import Path

# Apple stock
ticker = "AAPL"

# Download data
df = yf.download(ticker, period="30d")

# Fix MultiIndex columns
df.columns = [col[0] for col in df.columns]

# Convert Date from index to column
df = df.reset_index()

# Convert to JSON records
data = df.to_dict(orient="records")

# Bronze file path
bronze_path = Path("data/bronze/stock_raw.json")

# Save raw data
with open(bronze_path, "w") as f:
    json.dump(data, f, default=str, indent=4)

print("✅ Raw stock data saved")
print(f"Records: {len(data)}")
print(f"File: {bronze_path}")