import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("sales_data.csv")
monthList  = df['month_number'].tolist()
bathingsoapSalesData = df['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks(monthList)
plt.grid(True, linewidth=1, linestyle="--")
plt.title('Bathing soap sales data')
plt.savefig('sales_data_of_bathingsoap.png', dpi=150)
plt.show()