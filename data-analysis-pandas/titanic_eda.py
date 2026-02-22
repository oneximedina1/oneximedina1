import pandas as pd
import numpy as np

# Load Titanic dataset (from seaborn's hosted CSV)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=== Dataset Shape ===")
print(df.shape)

print("\n=== Missing Values ===")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Survival rate overall
survival_rate = df["Survived"].mean() * 100
print(f"\nOverall survival rate: {survival_rate:.1f}%")

# Survival rate by gender
print("\n=== Survival Rate by Gender ===")
print(df.groupby("Sex")["Survived"].mean().mul(100).round(1).astype(str) + "%")

# Survival rate by passenger class
print("\n=== Survival Rate by Class ===")
print(df.groupby("Pclass")["Survived"].mean().mul(100).round(1).astype(str) + "%")

# Age statistics
print("\n=== Age Statistics ===")
print(df["Age"].describe().round(1))

# Fill missing age with median and create age groups
df["Age"] = df["Age"].fillna(df["Age"].median())
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100],
                         labels=["Child", "Teen", "Adult", "Middle-aged", "Senior"])

print("\n=== Survival Rate by Age Group ===")
print(df.groupby("AgeGroup", observed=True)["Survived"].mean().mul(100).round(1).astype(str) + "%")
