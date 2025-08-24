# Load incident data
incidents = pd.read_csv('incident_data.csv')
severity = pd.read_csv('incident_severity.csv')  # Severity labeled 0-2: 0-low, 1-medium, 2-high

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(incidents, severity, test_size=0.3, random_state=42)

# Create and train the model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Predicting severity levels of incidents
predictions = svm_model.predict(X_test)

# Respond based on severity
for i, severity in enumerate(predictions):
    if severity == 2:  # High severity
        print(f"High severity incident detected: {incidents.iloc[i]}. Initiating response...")
        # Code to isolate or block the compromised system goes here
    elif severity == 1:  # Medium severity
        print(f"Medium severity incident detected: {incidents.iloc[i]}. Notifying security team...")
        # Code to notify security team...
    else:
        print(f"Low severity incident detected: {incidents.iloc[i]}. Monitoring...")
