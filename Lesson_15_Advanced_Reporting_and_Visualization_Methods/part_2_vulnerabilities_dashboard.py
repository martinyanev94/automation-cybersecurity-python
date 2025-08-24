import plotly.express as px
import pandas as pd

# Sample data for the dashboard
data = {
    'Category': ['Network', 'Application', 'Operating System', 'Database'],
    'Vulnerabilities': [40, 30, 20, 10]
}
df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='Category', y='Vulnerabilities', color='Vulnerabilities',
             title='Vulnerabilities by Category', labels={'Vulnerabilities': 'Number of Vulnerabilities'})
fig.show()
