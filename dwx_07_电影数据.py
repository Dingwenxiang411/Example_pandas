import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(1))


# 获取平均分
print(df["Rating"].mean())


# 获取导演的人数，unique自动将数据转换成列表，并且去除重复元素
# 下面的方法功能一样，tolist转换成列表，set去除重复元素
# print(len(df["Director"].unique()))
print(len(set(df["Director"].tolist())))


# 获取演员人数
# 获取以逗号分割的演员元素，并转换成列表（但这是列表套列表的形式）
temp_actor = df["Actors"].str.split(",").tolist()
print(temp_actor)
# 两重循环，将列表转换成单列表
actors_list = [i for j in temp_actor for i in j]
print(actors_list)
# set去除重复元素
print(len(set(actors_list)))


# 对rating，runtime分布情况进行分析
# 直方图
# 准备数据
runtime_data = df["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
rating_data = df["Rating"].values
max_rating = rating_data.max()
min_rating = rating_data.min()
# 计算组数
num_bin = (max_runtime - min_runtime)//5
# 设置不等宽的组距，hist方法取到的会是一个左闭右开的区间[1.9,3.5)
num_bin1 = [1.9, 3.5]
i = 3.5
while i <= max_rating:
    i += 0.5
    num_bin1.append(i)
# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)

# 分割绘图区域
plt.subplot(2, 1, 1)
plt.hist(runtime_data, num_bin)
# 绘制x轴
plt.xticks(range(min_runtime, max_runtime+5, 5))
# 绘制网格
plt.grid()
# # 分割绘图区域
plt.subplot(2, 1, 2)
plt.hist(rating_data, num_bin1)
# # TODO 绘制x轴，坐标轴不能识别0.5的精度
plt.xticks(range(len(num_bin1)), num_bin1)
plt.grid()
plt.show()
