import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n = 200

df = pd.DataFrame({
    "Age":        np.random.randint(22, 60, n),
    "Salary":     np.random.randint(30000, 120000, n),
    "Experience": np.random.randint(0, 35, n),
    "Score":      np.random.uniform(50, 100, n).round(1),
    "Hours/Week": np.random.randint(35, 60, n),
    "Projects":   np.random.randint(1, 20, n),
})

# Introduce some correlation
df["Salary"] = df["Salary"] + df["Experience"] * 1500
df["Score"]  = df["Score"]  + df["Projects"] * 1.2

corr = df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=0.5,
    ax=ax,
)
ax.set_title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()
print("Heatmap saved to correlation_heatmap.png")
