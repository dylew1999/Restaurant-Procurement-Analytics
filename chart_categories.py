import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kmyh_purchases_2022_anonymized.csv')
cats = pd.read_csv('item_categories.csv')

merged = df.merge(cats, on='item', how='left')
merged['category'] = merged['category'].fillna('Unclassified')

missing = merged[merged['category'].isna()]['item'].unique()
print("unmatched items:", missing)

cat = merged.groupby('category')['total_price'].sum().sort_values()
share = cat / cat.sum() * 100

plt.figure(figsize=(8, 5))
plt.barh(share.index, share.values)
plt.title('Share of procurement spend by category, 2022')
plt.xlabel('% of total spend')
plt.tight_layout()
plt.savefig('chart_categories.png', dpi=150)
plt.show()

print(share, round(1).to_string())
