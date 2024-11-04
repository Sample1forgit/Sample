import numpy as np
import pandas as pd

# Generate sample data
data = {
    'id': range(1, 101),
    'values': np.random.randint(1, 100, 100),  # Random values between 1 and 100
    'category': np.random.choice(['A', 'B', 'C'], 100)  # Random categories A, B, or C
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Calculate mean, median, and standard deviation for the 'values' column
mean_value = np.mean(df['values'])
median_value = np.median(df['values'])
std_dev = np.std(df['values'])

print("\nStatistics for the 'values' column:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev}")

# Example of group-by operation using pandas
category_stats = df.groupby('category')['values'].agg(['mean', 'median', 'std'])
print("\nStatistics by Category:")
print(category_stats)

