import pandas as pd
df = pd.read_csv("Automobile_data.csv")
most_expensive_car = df[['company', 'price']][df.price == df['price'].max()]
print("Most expensive car:")
print(most_expensive_car)