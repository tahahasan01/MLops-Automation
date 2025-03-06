import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv("student_data.csv")

# Convert 'Pass' and 'Fail' to binary values
data['result'] = data['result'].map({'Pass': 1, 'Fail': 0})

# Features and target
X = data[['study_hours', 'attendance', 'previous_score']]
y = data['result']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the model
joblib.dump(model, "model.py")