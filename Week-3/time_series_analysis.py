import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load Time Series Data (Example: Air Passenger Data)
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Display first few rows
print(df.head())

# Line Plot - Basic Trend
plt.figure(figsize=(12, 5))
plt.plot(df, marker='o', linestyle='-')
plt.title("Time Series Data - Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.grid(True)
plt.show()

# Rolling Average (Smoothing)
df['Rolling_Mean'] = df['Passengers'].rolling(window=12).mean()

plt.figure(figsize=(12, 5))
plt.plot(df['Passengers'], label="Original")
plt.plot(df['Rolling_Mean'], label="12-Month Rolling Mean", linestyle="dashed")
plt.title("Rolling Mean of Time Series Data")
plt.legend()
plt.grid(True)
plt.show()

# Decomposition (Trend, Seasonality, Residuals)
result = seasonal_decompose(df['Passengers'], model='additive', period=12)
result.plot()
plt.show()

# Autocorrelation (ACF) & Partial Autocorrelation (PACF)
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
plot_acf(df['Passengers'], ax=ax[0])
plot_pacf(df['Passengers'], ax=ax[1])
ax[0].set_title("Autocorrelation (ACF)")
ax[1].set_title("Partial Autocorrelation (PACF)")
plt.show()
