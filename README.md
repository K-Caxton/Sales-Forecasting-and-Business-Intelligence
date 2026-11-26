# Sales Forecasting and Business Intelligence

## Project Overview

This project analyzes historical retail sales data to identify business trends, evaluate profitability, and forecast future sales. It combines Python-based data analysis and time-series forecasting with business intelligence reporting.

## Objectives

- Clean and validate retail sales data.
- Explore sales and profitability patterns.
- Identify trends across product categories, regions, and customer segments.
- Compare forecasting models and select the best-performing model among those evaluated.
- Generate future sales forecasts to support business intelligence reporting.

## Tools and Technologies

- **Python:** Data cleaning, exploratory data analysis, and forecasting.
- **Pandas and NumPy:** Data manipulation and analysis.
- **Matplotlib and Seaborn:** Data visualization.
- **Statsmodels:** Time-series forecasting using SARIMA.
- **Power BI:** Interactive business intelligence dashboards.

## Data Analysis

The project uses the Sample Superstore retail dataset. The analysis includes data validation, monthly and annual sales trends, regional performance, category and subcategory profitability, customer segments, shipping methods, and the relationship between discounts and profits.

### Key Business Findings

- Total sales: approximately $2.30 million.
- Total profit: approximately $286,397.
- Overall profit margin: approximately 12.47%.
- The West region generated the highest sales.
- Technology generated the highest sales and category profit.
- Furniture profitability was considerably lower than that of the other main categories.
- Higher discounts were associated with lower profits in the dataset; this association does not establish causation.

## Sales Forecasting

Three forecasting approaches were evaluated:

1. Moving Average
2. Holt-Winters Exponential Smoothing
3. Seasonal Autoregressive Integrated Moving Average (SARIMA)

Models were compared using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

The original SARIMA configuration, with order (1, 1, 1) and seasonal order (1, 1, 1, 12), achieved the lowest MAE and RMSE among the three models on the selected test period. It was selected for the final forecast.

The forecasting script is located at `src/forecast_sales.py`. It loads the cleaned dataset, aggregates sales monthly, fits the selected SARIMA model, forecasts 12 months, and saves the predictions to `data/processed/sarima_sales_forecast.csv`.

### Forecasting Limitation

The historical dataset covers January 2014 to December 2017. Consequently, the generated forecast covers January to December 2018. It demonstrates the forecasting workflow and should not be interpreted as a current sales forecast.

## Project Status

Python data cleaning, exploratory data analysis, model comparison, and the final SARIMA forecasting workflow have been completed. Business intelligence reporting is part of the project's remaining work.

## Business Intelligence & Power BI

To make the analytical findings and SARIMA predictions accessible to business stakeholders, the processed datasets and forecast outputs are integrated into an interactive Power BI report.

- **Executive Overview:** Tracks high-level KPIs including total sales, total profit, profit margin, and year-over-year growth.
- **Category & Regional Drill-Downs:** Enables interactive filtering across product subcategories, customer segments, and geographic regions to pinpoint high-margin drivers and discount-heavy bottlenecks.
- **Forecast Visualization:** Combines historical monthly revenue (2014–2017) with the 12-month SARIMA sales projections (`sarima_sales_forecast.csv`) to highlight expected seasonal peaks. 