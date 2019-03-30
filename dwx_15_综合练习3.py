import pandas as pd
import matplotlib.pyplot as plt
# 不同年份书的数量
file_path = "./books.csv"
df = pd.read_csv(file_path)

print(df.info())
print(df.head(3))

# 注意出版年份中有数据缺失部分，要把缺失的数据删除
# TODO 如果在year_number增加[:20]就会出错
data1 = df[pd.notnull(df["original_publication_year"])]
year_number = (data1.groupby(by="original_publication_year").count()
               ["books_count"].sort_values(ascending=False))

_x = year_number.index
_y = year_number.values

plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y, width=0.3)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)
plt.show()

