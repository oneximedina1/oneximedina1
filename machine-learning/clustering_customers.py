import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 300

# Simulate customer data: annual income vs spending score
income  = np.concatenate([
    np.random.normal(30, 5, 80),
    np.random.normal(55, 8, 80),
    np.random.normal(80, 7, 80),
    np.random.normal(45, 6, 60),
])
spending = np.concatenate([
    np.random.normal(70, 8, 80),
    np.random.normal(50, 6, 80),
    np.random.normal(80, 7, 80),
    np.random.normal(25, 5, 60),
])

X = np.column_stack([income, spending])

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Find optimal K via inertia (elbow method)
inertias = []
K_range = range(2, 9)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

print("=== K-Means Customer Segmentation ===")
print("Inertia by K:")
for k, inertia in zip(K_range, inertias):
    print(f"  K={k}: {inertia:.2f}")

# Fit with K=4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

print("\nCluster sizes:")
unique, counts = np.unique(labels, return_counts=True)
for cluster, count in zip(unique, counts):
    mask = labels == cluster
    print(f"  Cluster {cluster}: {count} customers | "
          f"Avg Income: ${income[mask].mean():,.0f}K | "
          f"Avg Spending: {spending[mask].mean():.1f}")

# Plot
colors = ["steelblue", "tomato", "green", "orange"]
fig, ax = plt.subplots(figsize=(8, 6))
for cluster in unique:
    mask = labels == cluster
    ax.scatter(income[mask], spending[mask],
               c=colors[cluster], label=f"Cluster {cluster}", alpha=0.7)

ax.set_xlabel("Annual Income (K$)")
ax.set_ylabel("Spending Score")
ax.set_title("Customer Segmentation (K-Means, K=4)", fontweight="bold")
ax.legend()
plt.tight_layout()
plt.savefig("customer_clusters.png", dpi=150)
plt.show()
print("\nPlot saved to customer_clusters.png")
