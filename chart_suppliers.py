import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kmyh_purchases_2022_anonymized.csv', parse_dates=['date'])

spend = df.groupby('supplier')['total_price'].sum().sort_values()

plt.figure(figsize=(8, 5))
plt.barh(spend.index, spend.values)
plt.title('Total Spend by Supplier, 2022')
plt.xlabel('RM')
plt.tight_layout()
plt.savefig('chart_suppliers.png', dpi=150)
plt.show()
