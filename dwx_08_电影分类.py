import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#  TODO 这里包含了将字符串转换成数字的对应关系，这种思想在机器学习中非常重要
# 统计字符串的列表
temp_list = df["Genre"].str.split(",").tolist()  # 是一种列表嵌套列表的情况[[],[],[],[],.....]
genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)

# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    # 比如zero_df.loc[0, ["Action", "Sci-fi"]] = 1
    zero_df.loc[i, temp_list[i]] = 1

print(zero_df.head(3))
# 统计每个分类的电影的数量和
genre_count = zero_df.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()

# 画图
plt.figure(figsize=(20, 8), dpi=80)
_x = genre_count.index
_y = genre_count.values
plt.bar(range(len(_x)), _y, width=0.5)
plt.xticks(range(len(_x)), _x)
plt.show()
