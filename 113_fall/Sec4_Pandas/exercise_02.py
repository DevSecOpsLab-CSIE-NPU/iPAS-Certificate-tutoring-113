import pandas as pd
df = pd.read_csv("Automobile_data.csv", na_values={
    'price': ["?", "n.a"],
    'stroke': ["?", "n.a"],
    'horsepower': ["?", "n.a"],
    'peak-rpm': ["?", "n.a"],
    'average-mileage': ["?", "n.a"]
})
df.to_csv("Automobile_data.csv", index=False)
print("Cleaned dataset saved back to CSV.")