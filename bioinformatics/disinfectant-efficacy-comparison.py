# disinfectant-efficacy-comparison.py
# پروژه دانشجویی مقایسه کارایی ضدعفونی‌کننده با درصد کاهش

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# داده‌های نمونه (CFU/ml)
times = ['Before', 'After 5 min', 'After 10 min', 'After 30 min']
initial_count = 5.6e6
counts_after = [5.6e6, 82000, 3100, 12]

df = pd.DataFrame({
    'Time': times,
    'CFU_ml': counts_after
})

# محاسبات
df['log10_CFU'] = np.log10(df['CFU_ml'])
df['Log Reduction'] = np.log10(initial_count) - df['log10_CFU']
df['Percent Reduction'] = (1 - df['CFU_ml'] / initial_count) * 100

print("Disinfectant Efficacy Summary:")
print(df[['Time', 'CFU_ml', 'Log Reduction', 'Percent Reduction']].round(2))

# نمودار بهبودیافته
plt.figure(figsize=(9, 6))
plt.scatter(df['Time'], df['log10_CFU'], s=100, color='darkred', zorder=3)
plt.plot(df['Time'], df['log10_CFU'], linestyle='--', color='gray', alpha=0.7)
plt.title('Log₁₀ Bacterial Reduction After Disinfectant Exposure')
plt.xlabel('Exposure Time')
plt.ylabel('Log₁₀ (CFU/ml)')
plt.grid(True, alpha=0.3, linestyle=':')

# اضافه کردن متن روی نقاط
for i, row in df.iterrows():
    txt = f"{row['Log Reduction']:.2f} log\n({row['Percent Reduction']:.1f}%)"
    plt.annotate(txt, (row['Time'], row['log10_CFU'] + 0.15),
                 ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

plt.tight_layout()

# ذخیره و نمایش
plt.savefig('disinfectant-efficacy.png', dpi=150, bbox_inches='tight')
plt.show()
