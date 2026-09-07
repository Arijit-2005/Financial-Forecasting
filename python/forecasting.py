import pandas as pd
import matplotlib.pyplot as plt

# Load financial data
data = pd.read_csv("data/financial_data.csv")

# Display historical data
print("Historical Financial Data:")
print(data)

# Create forecast using average growth
last_revenue = data["Revenue"].iloc[-1]
last_expenses = data["Expenses"].iloc[-1]

revenue_growth = 0.03
expense_growth = 0.025

forecast = []

for month in range(1, 13):
    revenue = last_revenue * ((1 + revenue_growth) ** month)
    expenses = last_expenses * ((1 + expense_growth) ** month)
    profit = revenue - expenses

    forecast.append([month, revenue, expenses, profit])

forecast_df = pd.DataFrame(
    forecast,
    columns=["Month", "Forecast Revenue", "Forecast Expenses", "Forecast Profit"]
)

print("\n12-Month Financial Forecast:")
print(forecast_df)

# Save forecast
forecast_df.to_csv("financial_forecast_2027.csv", index=False)

# Create chart
plt.plot(forecast_df["Month"], forecast_df["Forecast Revenue"], label="Revenue")
plt.plot(forecast_df["Month"], forecast_df["Forecast Expenses"], label="Expenses")
plt.plot(forecast_df["Month"], forecast_df["Forecast Profit"], label="Profit")

plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Financial Forecast - 2027")
plt.legend()
plt.grid()

plt.savefig("financial_forecast.png")
plt.show()
