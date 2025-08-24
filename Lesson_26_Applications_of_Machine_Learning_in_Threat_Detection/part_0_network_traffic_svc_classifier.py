import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the dataset containing labeled network traffic information
data = pd.read_csv('network_traffic.csv')

# Features are all columns except the 'label'
X = data.drop('label', axis=1)  
# The label column, where '0' means benign and '1' means malicious
y = data['label']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating a Support Vector Classifier model
model = SVC(kernel='linear')
# Training the model on the training data
model.fit(X_train, y_train)

# Making predictions on the test set
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f'Model Accuracy: {accuracy * 100:.2f}%')
