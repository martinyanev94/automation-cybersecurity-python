import pandas as pd
from sklearn.ensemble import IsolationForest

# Load network traffic data
data = pd.read_csv('network_traffic.csv')

# Assume we have features: 'packet_size', 'destination_port', 'time_of_day'
X = data[['packet_size', 'destination_port', 'time_of_day']]

# Train the Isolation Forest model
model = IsolationForest(contamination=0.01)  # 1% of data as anomalies
model.fit(X)

# Predicting anomalies
data['anomaly'] = model.predict(X)
print(data[data['anomaly'] == -1])  # Display anomalies
