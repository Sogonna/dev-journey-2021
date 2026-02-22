# simple_cfu_comparison.py
# تکلیف میکروبیولوژی - مقایسه محیط‌های کشت

import pandas as pd
import matplotlib.pyplot as plt

# داده‌هایآزمایش (CFU/ml بعد از 24 ساعت)
data = {
    'Medium': ['LB', 'LB', 'LB', 'Nutrient Agar', 'Nutrient Agar', 'Nutrient Agar', 'TSA', 'TSA', 'TSA'],
    'CFU_ml': [2.3e8, 1.9e8, 2.5e8, 1.1e8, 1.4e8, 0.9e8, 1.8e8, 2.0e8, 1.7e8]
}

df = pd.DataFrame(data)

# میانگین و انحراف معیار
summary = df.groupby('Medium')['CFU_ml'].agg(['mean', 'std']).round(2)
print("میانگین و انحراف معیار CFU در هر محیط:")
print(summary)

# نمودار ستونی ساده
plt.figure(figsize=(7, 5))
plt.bar(summary.index, summary['mean'], yerr=summary['std'], capsize=5, color=['#4c72b0', '#55a868', '#c44e52'])
plt.title('مقایسه رشد باکتری در محیط‌های کشت مختلف')
plt.ylabel('CFU/ml (متوسط)')
plt.xlabel('محیط کشت')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

plt.savefig('cfu-micro-class.png', dpi=120)
plt.show()



