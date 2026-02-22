import pandas as pd
import numpy as np

# Sample sales data
data = {
    "date": pd.date_range(start="2024-01-01", periods=12, freq="MS"),
    "region": ["North", "South", "East", "West"] * 3,
    "sales": [15000, 22000, 18000, 9500, 17000, 24000,
              19500, 11000, 16000, 21000, 20000, 13000],
    "units": [150, 220, 180, 95, 170, 240, 195, 110, 160, 210, 200, 130],
}

df = pd.DataFrame(data)

# Summary statistics
print("=== Sales Summary ===")
print(df["sales"].describe())

# Total and average sales by region
print("\n=== Sales by Region ===")
region_summary = df.groupby("region").agg(
    total_sales=("sales", "sum"),
    avg_sales=("sales", "mean"),
    total_units=("units", "sum"),
).reset_index()
print(region_summary)

# Month with highest sales
best_month = df.loc[df["sales"].idxmax()]
print(f"\nBest month: {best_month['date'].strftime('%B %Y')} — ${best_month['sales']:,}")

# Monthly growth rate
df = df.sort_values("date")
df["growth_pct"] = df["sales"].pct_change() * 100
print("\n=== Monthly Growth (%) ===")
print(df[["date", "sales", "growth_pct"]].dropna().to_string(index=False))
