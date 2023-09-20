import pandas as pd

# Pandas - Data Correlations
# Finding Relationships

df = pd.read_csv('data.csv')

print(df.corr())



