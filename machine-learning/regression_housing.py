from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Train
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
mae  = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2   = r2_score(y_test, y_pred)

print("=== Linear Regression — California Housing ===")
print(f"MAE:  ${mae * 100_000:,.0f}")
print(f"RMSE: ${rmse * 100_000:,.0f}")
print(f"R²:   {r2:.4f}")

print("\nCoefficients (feature impact on price):")
for name, coef in sorted(
    zip(housing.feature_names, model.coef_), key=lambda x: abs(x[1]), reverse=True
):
    print(f"  {name}: {coef:+.4f}")
