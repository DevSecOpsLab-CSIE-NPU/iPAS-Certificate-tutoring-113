import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("sales_data.csv")
profitList = df['total_profit'].tolist()
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label='Profit data')
plt.xlabel('Profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()