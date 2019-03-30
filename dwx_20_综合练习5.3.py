import pandas as pd
import matplotlib.pyplot as plt
# 统计不同月份电话次数的变化情况

file_path = "./911.csv"
df = pd.read_csv(file_path)
# print(df.info())
# 将df中的timeStamp数据转换成pandas能识别的时间序列
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
# inplace的作用就是实现对原始数据的修改，因为作用函数本身没有返回值
df.set_index("timeStamp", inplace=True)
# df.set_index("timeStamp")
# print(df.head())
# df中数据按照月份进行统计，只要是数据不缺失的列都可以统计
count_by_month = df.resample("M").count()["title"]
print(count_by_month)

# 画图
_x = count_by_month.index
_y = count_by_month.values
# 将时间格式化，不然含有小时分钟
_x = [i.strftime("%Y-%m-%d") for i in _x]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.show()
