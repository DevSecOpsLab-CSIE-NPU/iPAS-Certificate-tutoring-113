import pandas as pd
df = pd.read_csv("Automobile_data.csv")
print("First 5 rows of the dataset:")
print(df.head(5))
print("\nLast 5 rows of the dataset:")
print(df.tail(5))