from sklearn.ensemble import IsolationForest

# Load pre-processed network traffic data
network_data = pd.read_csv('cleaned_network_traffic.csv')

# Features are all the columns except the last column which might be the label
features = network_data.iloc[:, :-1]

# Create an Isolation Forest model
model = IsolationForest(contamination=0.05)  # We assume that 5% of the data may be anomalies
# Fitting the model to the features
model.fit(features)

# Predicting anomalies, with -1 indicating outliers and 1 indicating normal instances
anomalous_predictions = model.predict(features)

# Extracting the anomalous data points for further investigation
anomalous_data = network_data[anomalous_predictions == -1]
print("Anomalous Data Points:")
print(anomalous_data)
