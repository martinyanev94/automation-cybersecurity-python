import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load incident data and severity levels
incidents = pd.read_csv('incident_data.csv')
severity = pd.read_csv('incident_severity.csv')  # Severity labeled from 0-2: 0-low, 1-medium, 2-high

# Split the dataset into features and labels
X = incidents
y = severity['Severity']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Making predictions on the test set
predictions = model.predict(X_test)

# Act based on severity
for i, severity in enumerate(predictions):
    if severity == 2:  # High severity
        print(f"High severity incident detected: {incidents.iloc[i]}. Initiating response...")
        # Here, code to isolate or block the compromised system would go.
    elif severity == 1:  # Medium severity
        print(f"Medium severity incident detected: {incidents.iloc[i]}. Notifying security team...")
        # Code to notify the security team goes here...
    else:
        print(f"Low severity incident detected: {incidents.iloc[i]}. Monitoring...")
