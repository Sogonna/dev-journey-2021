# disinfectant-log-reduction.py
# محاسبه log reduction بعد از استفاده از ضدعفونی‌کننده

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# داده‌های قبل و بعد ضدعفونی (CFU/ml)
times = ['قبل', 'بعد 5 دقیقه', 'بعد 10 دقیقه', 'بعد 30 دقیقه']
counts_before = 5.6e6
counts_after = [5.6e6, 8.2e4, 3.1e3, 1.2e1]  # کاهش شدید

df = pd.DataFrame({
    'زمان': times,
    'CFU_ml': counts_after
})

# محاسبه log10
df['log_CFU'] = np.log10(df['CFU_ml'])

# log reduction نسبت به قبل
df['log_reduction'] = np.log10(counts_before) - df['log_CFU']

print(df[['زمان', 'CFU_ml', 'log_reduction']])

# نمودار
plt.figure(figsize=(8, 5))
plt.plot(df['زمان'], df['log_CFU'], marker='o', linestyle='-', color='darkred')
plt.title('کاهش لگاریتمی باکتری بعد از ضدعفونی')
plt.ylabel('log10 (CFU/ml)')
plt.grid(True, alpha=0.3)

for i, txt in enumerate(df['log_reduction'].round(2)):
    plt.annotate(f'کاهش {txt} log', (df['زمان'][i], df['log_CFU'][i]+0.1))

plt.tight_layout()
plt.savefig('log-reduction-disinfectant.png', dpi=130)
plt.show()


