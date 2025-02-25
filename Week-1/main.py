import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# Load the dataset
df = pd.read_csv("emails.csv")

# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Display basic information
print(df.info())
print(df.describe())

# 1. Bar Chart - Number of Emails per Sender
plt.figure(figsize=(10, 5))
df["sender"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Number of Emails per Sender")
plt.xlabel("Sender")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 2. Pie Chart - Spam vs Not Spam
spam_counts = df["label"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(spam_counts, labels=spam_counts.index, autopct="%1.1f%%", colors=["red", "green"], startangle=90)
plt.title("Spam vs Not Spam")
plt.show()

# 3. Word Cloud - Most Common Words in Subject Lines
subject_text = " ".join(df["subject"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(subject_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Email Subjects")
plt.show()

# Heatmap - Correlation Matrix (Only if Numeric Columns Exist)
numeric_df = df.select_dtypes(include=['number'])  
if not numeric_df.empty:
    plt.figure(figsize=(8, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix Heatmap")
    plt.show()
else:
    print("No numeric columns found, skipping heatmap.")

# 5. Histogram - Emails Sent Over Time
plt.figure(figsize=(10, 5))
df["timestamp"].dt.date.value_counts().sort_index().plot(kind="bar", color="purple")
plt.title("Email Distribution Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Emails")
plt.xticks(rotation=45)
plt.show()

# Boxplot for Email Counts per Sender (Fix)
plt.figure(figsize=(10, 5))
sender_counts = df["sender"].value_counts().reset_index()
sender_counts.columns = ["sender", "count"]

sns.boxplot(x="sender", y="count", data=sender_counts, palette="coolwarm")
plt.xticks(rotation=90)  
plt.title("Distribution of Emails per Sender")
plt.show()
