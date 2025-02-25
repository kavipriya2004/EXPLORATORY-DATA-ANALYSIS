import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the wine quality dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_data = pd.read_csv(url, delimiter=";")

# Display basic information
print(wine_data.info())
print(wine_data.describe())

# Check for missing values
print("Missing Values:\n", wine_data.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(wine_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Wine Quality Features")
plt.show()

# Histogram of wine quality
sns.countplot(x="quality", data=wine_data, palette="Set2")
plt.title("Distribution of Wine Quality Ratings")
plt.show()

# Boxplot of acidity vs. quality
sns.boxplot(x="quality", y="volatile acidity", data=wine_data, palette="Set3")
plt.title("Volatile Acidity vs. Wine Quality")
plt.show()

print("EDA on Wine Quality dataset completed successfully.")
