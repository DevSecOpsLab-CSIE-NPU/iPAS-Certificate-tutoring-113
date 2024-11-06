import pandas as pd
df = pd.read_csv("Automobile_data.csv")
average_mileage = df.groupby('company')['average-mileage'].mean()
print("Average mileage of each car making company:")
print(average_mileage)