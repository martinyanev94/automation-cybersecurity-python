import pandas as pd

# Example performance data
data = pd.DataFrame({
    'action': ['block', 'notify', 'block', 'ignore'],
    'result': ['success', 'success', 'failure', 'success']
})

success_rate = data['result'].value_counts(normalize=True)['success']
print(f"Automation Success Rate: {success_rate:.2%}")
