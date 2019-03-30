import pandas as pd
import numpy as np
# 统计不同类型的紧急情况的次数

file_path = "./911.csv"
df = pd.read_csv(file_path)
# print(df.head(2))
# print(df.info())

# 获取分类，series中tolist没有下划线
temp_list = df["title"].str.split(":").tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)

# 赋值
for cate in cate_list:
    # contains函数就是包含的话就为真，否则为假
    zeros_df[cate][df["title"].str.contains(cate)] = 1
print(zeros_df)
# # 还有一种执行速度非常慢的程序
# for i in range(df.shape[0]):
#     zeros_df.loc[i, temp_list[i][0]] = 1
# print(zeros_df)

# 求和，统计
sum_ret = zeros_df.sum(axis=0)
print(sum_ret)
