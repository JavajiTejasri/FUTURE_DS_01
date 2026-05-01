import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print(df.head())

df['Revenue'] = df['total_bill']

daily_sales = df.groupby('day')['Revenue'].sum()
daily_sales.plot(kind='bar', title='Revenue by Day')
plt.show()

group_sales = df.groupby('size')['Revenue'].sum()
group_sales.plot(kind='bar', title='Revenue by Group Size')
plt.show()

gender_sales = df.groupby('sex')['Revenue'].sum()
gender_sales.plot(kind='bar', title='Revenue by Gender')
plt.show()