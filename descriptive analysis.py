# Descriptive Analysis
# Rising Waters Project

import pandas as pd

# Reading the dataset
    # Change the file name if needed 
data = pd.read_excel("flood dataset.xlsx")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

print("\n")

# Basic information about the dataset
print("Dataset Information:")
data.info()

print("\n")

# Statistical summary
print("Summary Statistics:")
print(data.describe())

print("\n")

# Checking for missing values
print("Missing Values:")
print(data.isnull().sum())

print("\n")

# Checking data types
print("Data Types:")
print(data.dtypes)

print("\n")

# Dataset dimensions
print("Dataset Shape:")
print(data.shape)

print("\n")

# Column names
print("Column Names:")
print(data.columns)