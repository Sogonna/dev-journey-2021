import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# داده‌های نمونه (OD = Optical Density)
data = {
    'Time_hours': [0, 1, 2, 3, 4, 5, 6, 7, 8],
    'OD_control': [0.05, 0.08, 0.15, 0.35, 0.82, 1.45, 1.80, 1.92, 1.95],
    'OD_antibiotic': [0.05, 0.06, 0.09, 0.12, 0.18, 0.25, 0.32, 0.35, 0.36]
}

df = pd.DataFrame(data)

# رسم نمودار
plt.figure(figsize=(10, 6))
plt.plot(df['Time_hours'], df['OD_control'], 'o-', label='بدون آنتی‌بیوتیک')
plt.plot(df['Time_hours'], df['OD_antibiotic'], 's-', label='با آنتی‌بیوتیک')
plt.xlabel('زمان (ساعت)')
plt.ylabel('OD600')
plt.title('منحنی رشد باکتری')
plt.legend()
plt.grid(True, alpha=0.3)

# نمایش نمودار
plt.show()



