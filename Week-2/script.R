# Load libraries
library(ggplot2)
library(dplyr)

# Creating sample data
data <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David"),
  Age = c(25, 30, 35, 40),
  Salary = c(50000, 60000, 70000, 80000)
)

print("Original Data:")
print(data)

# Filtering Data
filtered_data <- filter(data, Age > 28)
print("Filtered Data:")
print(filtered_data)

# Visualization
ggplot(data, aes(x = Age, y = Salary)) +
  geom_point(color = "blue", size = 3) +
  labs(title = "Age vs Salary", x = "Age", y = "Salary") +
  theme_minimal()
