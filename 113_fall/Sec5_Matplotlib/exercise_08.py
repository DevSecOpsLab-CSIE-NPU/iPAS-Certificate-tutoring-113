import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("sales_data.csv")
labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), 
             df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()