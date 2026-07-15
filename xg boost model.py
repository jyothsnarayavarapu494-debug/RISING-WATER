import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Read the dataset
data = pd.read_excel("flood dataset.xlsx")

# Create X and y
X = data.drop("flood", axis=1)
y = data["flood"]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10
)

# Create the model
model = GradientBoostingClassifier()

# Train the model
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))