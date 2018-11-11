import pandas as pd

# Create a data frame reference
df = pd.read_csv('data/example.csv')

# Print out any employee whose salary is above 80
print(df[df['salary'] > 80])
