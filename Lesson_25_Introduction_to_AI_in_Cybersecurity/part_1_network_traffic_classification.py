import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset containing network traffic information
data = pd.read_csv('network_traffic.csv')

# Assuming 'label' column has '0' for benign and '1' for malicious
X = data.drop('label', axis=1)  # Features
y = data['label']                # Labels

# Splitting the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Support Vector Classifier model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f'Model Accuracy: {accuracy * 100:.2f}%')
