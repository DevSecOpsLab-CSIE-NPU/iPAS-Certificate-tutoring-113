import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
carsDf1 = pd.DataFrame(GermanCars)
carsDf2 = pd.DataFrame(japaneseCars)
carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
print("Concatenated DataFrames:")
print(carsDf)