
from pathlib import Path
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Project paths
project_dir = Path(__file__).resolve().parent.parent

data_path = project_dir / "data" / "processed" / "superstore_cleaned.csv"
output_path = project_dir / "data" / "processed" / "sarima_sales_forecast.csv"
model_dir = project_dir / "models"
model_path = model_dir / "sarima_sales_model.pkl"

# Create models folder if it doesn't exist
model_dir.mkdir(parents=True, exist_ok=True)

# Load cleaned data
store_data = pd.read_csv(data_path, encoding="latin1")
store_data["Order Date"] = pd.to_datetime(store_data["Order Date"])

# Aggregate monthly sales
monthly_sales = (
    store_data.set_index("Order Date")["Sales"]
    .resample("MS")
    .sum()
)

# Fit the selected SARIMA model
sarima_model = SARIMAX(
    monthly_sales,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12),
    enforce_stationarity=False,
    enforce_invertibility=False
).fit(disp=False)

# Save the fitted model
sarima_model.save(model_path)

# Forecast the next 12 months
future_forecast = sarima_model.forecast(steps=12)

# Prepare forecast output
forecast_df = pd.DataFrame({
    "Forecast Date": future_forecast.index,
    "Forecast Sales": future_forecast.values
})

forecast_df["Forecast Sales"] = forecast_df["Forecast Sales"].round(2)

# Save forecast results
forecast_df.to_csv(output_path, index=False)

print("Forecast generated successfully!")
print(f"Model saved to: {model_path}")
print(f"Forecast saved to: {output_path}")


