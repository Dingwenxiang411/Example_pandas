import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
print(t)
print(" " * 50)
# # 通过标签获取数据
# print(t.loc["a", "Z"])
# print(" " * 50)
# print(t.loc[["a", "c"]])
# print(t.loc[:, ["W", "Z"]])
# # 通过位置获取数据
print(t.iloc[1])
