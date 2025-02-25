import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# NumPy Operations
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("NumPy Array:\n", arr)
print("Shape of array:", arr.shape)
print("Sum of elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))

# Pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

# Filtering in Python
filtered_df = df[df['Age'] > 28]
print("Filtered DataFrame:\n", filtered_df)

# 1️⃣ Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="Sine Wave", color='blue')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Plot using Matplotlib")
plt.legend()
plt.show()

# 2️⃣ Scatter Plot
plt.scatter(df['Age'], df['Salary'], color='red', marker='o')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary Scatter Plot")
plt.show()

# 3️⃣ Bar Chart
plt.bar(df['Name'], df['Salary'], color=['blue', 'green', 'orange'])
plt.xlabel("Name")
plt.ylabel("Salary")
plt.title("Salary Comparison")
plt.show()

# 4️⃣ Histogram
plt.hist(df['Age'], bins=5, color='purple', edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution Histogram")
plt.show()

# 5️⃣ Pie Chart
plt.pie(df['Salary'], labels=df['Name'], autopct='%1.1f%%', colors=['red', 'blue', 'green'])
plt.title("Salary Distribution")
plt.show()

# Call the R script
subprocess.run(["Rscript", "script.R"])
