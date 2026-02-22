import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [15000, 18200, 22000, 19500, 24000, 27500,
         23000, 25800, 21000, 28000, 31000, 35000]

x = np.arange(len(months))

fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart
bars = ax.bar(x, sales, color="steelblue", alpha=0.8, label="Monthly Sales")

# Trend line
z = np.polyfit(x, sales, 1)
p = np.poly1d(z)
ax.plot(x, p(x), color="tomato", linewidth=2, linestyle="--", label="Trend")

# Labels on bars
for bar, value in zip(bars, sales):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 300,
            f"${value:,}",
            ha="center", va="bottom", fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(months)
ax.set_ylabel("Sales ($)")
ax.set_title("Monthly Sales Dashboard — 2024", fontsize=14, fontweight="bold")
ax.legend()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax.set_ylim(0, max(sales) * 1.15)

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=150)
plt.show()
print("Chart saved to sales_dashboard.png")
