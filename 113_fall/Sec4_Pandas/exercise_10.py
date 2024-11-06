import pandas as pd
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
carPriceDf = pd.DataFrame(Car_Price)
carHorsepowerDf = pd.DataFrame(car_Horsepower)
carsDf = pd.merge(carPriceDf, carHorsepowerDf, on="Company")
print("Merged DataFrame:")
print(carsDf)