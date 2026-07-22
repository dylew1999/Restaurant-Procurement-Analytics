import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kmyh_purchases_2022_anonymized.csv', parse_dates=['date'])
rev = pd.read_csv('revenue_2022.csv')

spend = df.groupby(df['date'].dt.month)['total_price'].sum()
ratio = spend.values / rev['revenue'].values * 100

print("Annual ratio: %.1f%%" % (spend.sum() / rev['revenue'].sum() * 100))

plt.figure(figsize=(9, 5))
plt.axhspan(35, 45, alpha=0.15, color='green')
plt.plot(rev['month'], ratio, marker='o')
plt.title('Purchases as % of revenue, 2022')
plt.xlabel('Month')
plt.ylabel('% of revenue')
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart_cogs_ratio.png', dpi=150)
plt.show()
