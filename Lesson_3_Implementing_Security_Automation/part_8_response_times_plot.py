import matplotlib.pyplot as plt

# Sample data
prior_response_times = [120, 90, 150, 110, 100]  # In seconds
post_response_times = [30, 20, 25, 35, 28]  # In seconds

plt.plot(prior_response_times, label='Prior Response Times', marker='o')
plt.plot(post_response_times, label='Post Automation Response Times', marker='x')
plt.title('Incident Response Times Before and After Automation')
plt.xlabel('Incident Number')
plt.ylabel('Response Time (seconds)')
plt.legend()
plt.show()
