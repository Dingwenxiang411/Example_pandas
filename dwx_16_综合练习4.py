import pandas as pd
import matplotlib.pyplot as plt
# 不同年份书的评分情况
file_path = "./books.csv"
df = pd.read_csv(file_path)

# 去除original_publication_year中的nan部分
data1 = df[pd.notnull(df["original_publication_year"])]

# 以下两种方式输出结果相同
# rating_count = data1.groupby(by="original_publication_year").mean()["average_rating"]
rating_count = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(rating_count)
_x = rating_count.index
_y = rating_count.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)
# 坐标轴太集中，可以选择步长，astype将年份转换成int类型
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)
plt.show()
