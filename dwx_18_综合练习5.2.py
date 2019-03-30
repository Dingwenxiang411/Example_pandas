import pandas as pd
import numpy as np
# 统计不同类型的紧急情况的次数

file_path = "./911.csv"
df = pd.read_csv(file_path)
# print(df.head(2))
# print(df.info())

# 将提取出来的数据单独插入到df后面
temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
# 要给一个DataFrame插入数据，直接指定新的索引名就可以了
df["cate"] = cate_df
# print(df.head(5))
# 通过cate分类，然后再依据分类统计数量，再取出一列，所以这一列是哪一列都无所谓
print(df.groupby(by="cate").count()["title"])
