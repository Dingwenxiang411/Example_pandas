import pandas as pd
import numpy as np

# 使数据按照列索引进行合并
t1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=["x", "y", "z"])
t2 = pd.DataFrame(np.ones((2, 4)), columns=["1", "2", "y", "3"])
t2.loc[1, "3"] = 9
print(t1)
print(t2)

# 以t1的"y"为合并轴，t2的"y"中若有与之相同的元素，就合并该行元素
# t1中元素放在左侧，t2中除了"y"列元素，其他放在右侧
# 注意广播机制，t2中"y"列有两个元素与t1中相等
# 这种方式为内连接，取交集
print(t1.merge(t2, on="y"))
# 外连接，取并集
print(t1.merge(t2, on="y", how="outer"))
# 左连接，以左边为准
print(t1.merge(t2, on="y", how="left"))
# 右连接，以右边为准
print(t1.merge(t2, on="y", how="right"))
# print(t2.merge(t1, on="y"))
