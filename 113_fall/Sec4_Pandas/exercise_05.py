import pandas as pd
df = pd.read_csv("Automobile_data.csv")
print("Total cars per company:")
print(df['company'].value_counts())