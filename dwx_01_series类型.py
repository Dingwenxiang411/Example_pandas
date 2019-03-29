import pandas as pd
import string
t = pd.Series([1, 2, 3, 51, 6, 9])
print(t)
# 指定索引
t1 = pd.Series([1, 5, 9, 62, 52, 65], index=list("abcdef"))
print(t1)
# 通过字典来创建Series
temp_dict = {"name": "xiaohong", "age": 30, "phone": 10086}
t2 = pd.Series(temp_dict)
print(t2)
# 用string库创建字典，导入Series
a = {string.ascii_uppercase[i]: i for i in range(10)}
print(pd.Series(a))
# Series的切片和索引（用索引名和位置都可以） 
print(t2["name"])
print(t2[2])
print(t[[1, 3, 4]])  # 取索引位置1，3，4的元素
print(t[2:])  # 取索引号2及后面所有元素
print(t[t > 4])  # 取t中大于4的元素
# 输出Series中的数据和索引
print(t2.index)
print(t2.values)
