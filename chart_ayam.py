import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kmyh_purchases_2022_anonymized.csv', parse_dates=['date'])

ayam = df[df['item'] == 'Ayam']
unit_price = df['unit_price']
monthly = ayam.groupby(ayam['date'].dt.month)['unit_price'].mean()

plt.figure(figsize=(8, 4.5))
plt.plot(monthly.index, monthly.values, marker='o')
plt.title('Ayam average price, 2022')
plt.xlabel('Month')
plt.ylabel('RM per kg')
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart_ayam_price.png', dpi=150)
plt.show()
