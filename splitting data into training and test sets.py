# Splitting the dataset into X and y

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the dataset
data = pd.read_excel("flood dataset.xlsx")

# Independent variables (Input)
X = data.drop("flood", axis=1)

# Dependent variable (Output)
y = data["flood"]

print("Independent Variables (X):")
print(X.head())

print("\nDependent Variable (y):")
print(y.head())

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=10
)

print("\nTraining Data Shape:", x_train.shape)
print("Testing Data Shape:", x_test.shape)

print("\nTraining Labels Shape:", y_train.shape)
print("Testing Labels Shape:", y_test.shape)