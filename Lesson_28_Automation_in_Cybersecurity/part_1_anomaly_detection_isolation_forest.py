import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

# Load sample data
data = pd.read_csv("security_events.csv")

# Separating features and labels
X = data.drop('label', axis=1)  # Features
y = data['label']                # Labels
# Splitting the dataset into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Initializing the model
model = IsolationForest(contamination=0.1)
model.fit(X_train)

# Making predictions on the test set
predictions = model.predict(X_test)

# Convert predictions to a more readable format
predictions = [1 if p == -1 else 0 for p in predictions]  # -1 for anomaly, 0 for normal
