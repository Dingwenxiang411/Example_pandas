import pandas as pd
import numpy as np

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# print(df.head(3))
# print(df.info())

t1 = df.groupby(by="Country")  # 输出一个DataFrameGroupby的对象

# 对于DataFrameGroupby可以进行遍历也可以用调用聚合方法
# t1已经按照国家进行了分组，相同的国家的都放在同一个元祖中
# for i in t1:
#     print(i)
#     print("*" * 50)
# 取出Country为"US"的元素
# print(df[df["Country"] == "US"])  # 不要需要遍历，直接用逻辑判断的简单写法

# 调用聚合方法，统计中国和美国的星巴克数量
# print(t1.count())  # 这个操作的作用，按照Country进行分类，统计其他特征的数量
country_count = t1["Brand"].count()  # 这个操作的作用，按照Country进行分类，统计Brand特征的数量
print(country_count["US"])  # 取出"US"的Brand数量
print(country_count["CN"])  # 取出"CN"的Brand数量

# 统计中国各个省份的星巴克数量
# chian_data = df[df["Country"] == "CN"]
# t2 = chian_data.groupby(by="State/Province")
# print(t2.count()["Brand"])

# 数据按照多个条件进行分组
grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
print(grouped)
print(type(grouped))  # 可以看出grouped是一个series类型，但是他的索引有两列
# grouped = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))  # 可以看出grouped是一个dataframe类型，在df["Brand"]加了一对方括号

# 和上面的区别是，在整个大数据下，是由"Country"和"State/Province"的数据的
# grouped1 = df.groupby(by=["Country", "State/Province"]).count()
# print(grouped1)
print("*" * 50)

# 索引的方法和属性
print(grouped.index)
