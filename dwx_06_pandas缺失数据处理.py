import numpy as np
import pandas as pd

t = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
t.iloc[1:, :2] = np.NaN
print(t)
# # 删除NaN所在的行列
# # 其中how="all"表示整行或者整列都为NaN才删除
# print(t.dropna(axis=0, how="all"))
# # 其中how="any"表示行或者列有NaN就删除
# print(t.dropna(axis=0, how="any"))
# print(t)
# print(" " * 50)
# # inplace表示原地修改，如果不实行，参数本身不会被修改
# print(t.dropna(axis=0, how="any", inplace=True))
# print(t)

# 修改NaN的值
print(t.fillna(t.mean()))
# 单独对某一列进行操作
t["W"] = t["W"].fillna(t["W"].mean())
print(t)
