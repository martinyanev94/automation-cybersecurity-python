from sklearn.ensemble import IsolationForest

# Load pre-processed network traffic data
network_data = pd.read_csv('cleaned_network_traffic.csv')

# Separating features
features = network_data.iloc[:, :-1]

# Fit the Isolation Forest model to the features
model = IsolationForest(contamination=0.05)  # Assuming 5% of the data may be anomalies
model.fit(features)

# Predicting anomalies
anomalous_predictions = model.predict(features)

# Extracting the anomalous data points
anomalous_data = network_data[anomalous_predictions == -1]
print("Anomalous Data Points:")
print(anomalous_data)
