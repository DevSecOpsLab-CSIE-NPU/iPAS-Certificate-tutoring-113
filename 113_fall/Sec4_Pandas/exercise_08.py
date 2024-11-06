import pandas as pd
df = pd.read_csv("Automobile_data.csv")
sorted_cars = df.sort_values(by=['price'], ascending=False)
print("Cars sorted by price:")
print(sorted_cars.head(5))