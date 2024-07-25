import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kc_house_data.csv')

# Show just column
for col in df.columns:
    print(col)

df['price'].plot.hist(bins=30, edgecolor='black')

print(df[['price', 'waterfront']])

plt.show()