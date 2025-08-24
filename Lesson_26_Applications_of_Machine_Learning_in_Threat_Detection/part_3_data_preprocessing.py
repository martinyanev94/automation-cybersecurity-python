# Load your dataset
data = pd.read_csv('network_traffic.csv')

# Checking for missing values
missing_values = data.isnull().sum()
print("Missing Values per Column:")
print(missing_values)

# Filling missing values with the median (for numerical data)
data.fillna(data.median(), inplace=True)

# Removing duplicate entries
data.drop_duplicates(inplace=True)

# Verifying data types 
print("Data Types:")
print(data.dtypes)
