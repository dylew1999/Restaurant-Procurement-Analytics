import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kmyh_purchases_2022_anonymized.csv', parse_dates=['date'])

monthly = df.groupby(df['date'].dt.month)['total_price'].sum()

plt.figure(figsize=(8, 4.5))
plt.plot(monthly.index, monthly.values, marker='o')
plt.title('Monthly Spend of the year, 2022')
plt.xlabel('Month')
plt.ylabel('RM(ringgit Malaysia)')
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chart_monthly_spend.png', dpi=150)
plt.show()
