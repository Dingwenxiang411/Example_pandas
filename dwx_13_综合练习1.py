import pandas as pd
import matplotlib.pyplot as plt

# 使用matplotlip呈现店铺总数排名前十的国家
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

print(df.info())
country_data = df.groupby(by="Country")
print(country_data)
country_brand_count = country_data["Store Number"].count().sort_values(ascending=False)[:10]
print(country_brand_count)

_x = country_brand_count.index
_y = country_brand_count.values

plt.figure(figsize=(20, 8), dpi=80)
plt.xticks(range(len(_x)), _x)
plt.bar(range(len(_x)), _y)
plt.show()
