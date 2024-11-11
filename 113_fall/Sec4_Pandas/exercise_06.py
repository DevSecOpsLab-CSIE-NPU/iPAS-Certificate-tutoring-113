import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
highest_price_cars = car_Manufacturers[['company', 'price']].max()
print("Each company's highest price car:")
print(highest_price_cars)