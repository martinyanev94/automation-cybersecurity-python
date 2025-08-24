import matplotlib.pyplot as plt

# Sample data for monthly patching compliance over six months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
patched_vulnerabilities = [15, 28, 35, 50, 65, 80]

# Plotting the trend
plt.figure(figsize=(10, 5))
plt.plot(months, patched_vulnerabilities, marker='o', color='green', linestyle='-')
plt.title('Vulnerabilities Patched Over Time')
plt.xlabel('Months')
plt.ylabel('Number of Patched Vulnerabilities')
plt.grid(True)
plt.xticks(months)
plt.show()
