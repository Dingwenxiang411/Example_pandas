import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 使用matplotlib呈现每个中国城市的店铺数量

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.info())
df = df[df["Country"] == "CN"]

store_city_data = df.groupby(by="City").count()["Store Number"].sort_values(ascending=False)[:50]

_x = store_city_data.index
_y = store_city_data.values

plt.figure(figsize=(20, 8), dpi=80)
font_ticks = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=10)
plt.xticks(range(len(_x)), _x, fontproperties=font_ticks, rotation=45)
plt.bar(range(len(_x)), _y, width=0.5)
plt.show()
