import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Debug: Print current working directory
print("Current Working Directory:", os.getcwd())

# Path to the CSV file (relative to the script's location)
csv_path = os.path.join(os.path.dirname(__file__), "student_data.csv")

# Debug: Check if the CSV file exists
if not os.path.exists(csv_path):
    print(f"Error: File '{csv_path}' not found.")
else:
    print(f"File '{csv_path}' found. Loading data...")

# Load the dataset
data = pd.read_csv(csv_path)

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
joblib.dump(model, "student_model.pkl")

# Function to load the model and make predictions
def predict(input_data):
    # Load the model
    model = joblib.load("student_model.pkl")
    
    # Make prediction
    prediction = model.predict([input_data])
    
    # Return 'Pass' or 'Fail' based on the prediction
    return 'Pass' if prediction[0] == 1 else 'Fail'