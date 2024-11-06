import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("sales_data.csv")
monthList  = df['month_number'].tolist()
plt.stackplot(monthList, df['facecream'], df['facewash'], df['toothpaste'], 
              df['bathingsoap'], df['shampoo'], df['moisturizer'], 
              colors=['m','c','r','k','g','y'])
plt.xlabel('Month Number')
plt.ylabel('Sales units in Number')
plt.title('All product sales data using stack plot')
plt.legend(['face Cream', 'Face wash', 'Tooth paste', 'Bathing soap', 'Shampoo', 'Moisturizer'], loc='upper left')
plt.show()