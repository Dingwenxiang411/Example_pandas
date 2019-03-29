import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape(3, 4))
print(t)
# 指定行索引和列索引
t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
print(t1)
# 用字典传入数据
a1 = {"name": ["xiaohong", "wangeu"], "age": [18, 22], "phone": [10086, 10000]}
t2 = pd.DataFrame(a1)
print(t2)
a2 = [{"name": "xiaohong", "age": 18, "tel": 10086}, {"name": "xiaowang", "tel": 10000},
      {"name": "xiaogang", "tel": 10010}]
t3 = pd.DataFrame(a2)
print(t3)
# 输出DataFrame的一些属性
print(t3.values)
print(t3.dtypes)
print(t3.index)
print(t3.columns)
# 显示前几行
print(t3.head(2))
print(" " * 50)
# 显示后几行
print(t3.tail(1))
print(" " * 50)
# 显示DataFrame的信息
print(t3.info())
print(" " * 50)
# 显示DataFrame的最大值、最小值、方差（针对数字）等
print(t3.describe())



