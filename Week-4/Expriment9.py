import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load COVID-19 dataset (Example)
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Select relevant columns
covid_data = covid_data[["date", "location", "total_cases", "total_deaths", "population"]]

# Convert date to datetime format
covid_data["date"] = pd.to_datetime(covid_data["date"])

# Filter for India
india_data = covid_data[covid_data["location"] == "India"]

# Plot total cases over time
plt.figure(figsize=(12, 6))
plt.plot(india_data["date"], india_data["total_cases"], label="Total Cases", color="blue")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("COVID-19 Cases Over Time in India")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Scatter plot for cases vs deaths
sns.scatterplot(x="total_cases", y="total_deaths", data=india_data, color="red")
plt.title("Total Cases vs Total Deaths in India")
plt.show()

# Death rate over time
india_data["death_rate"] = (india_data["total_deaths"] / india_data["total_cases"]) * 100
plt.figure(figsize=(10, 5))
sns.lineplot(x="date", y="death_rate", data=india_data, color="green")
plt.title("Death Rate Over Time in India")
plt.xlabel("Date")
plt.ylabel("Death Rate (%)")
plt.show()

print("Case study analysis completed successfully.")
