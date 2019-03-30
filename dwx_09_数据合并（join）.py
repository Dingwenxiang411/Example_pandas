import pandas as pd
import numpy as np

# 使数据按照行索引进行合并
# TODO zeros()和ones()必须传入元祖
# TODO 列表中传入数字和字符串的时候要注意：[“0123”]代表一个字符；[0,1,2,3]代表四个字符
# TODO ["abcd"]为一个字符；["a","b","c","d"]代表四个字符，即list会区分，[]不会区分
t1 = pd.DataFrame(np.zeros((2, 4)), index=list("AB"), columns=[0, 1, 2, 3])
t2 = pd.DataFrame(np.ones((3, 3)), index=["A", "B", "C"], columns=list("456"))
# print(t1)
# print(t2)
print(t1.join(t2))
print(t2.join(t1))
