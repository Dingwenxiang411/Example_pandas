import pandas as pd

df = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())

# dataframe中排序的fangfa，默认升序，可以用ascending来使其逆序
# 按照某一列进行排序
# df = df.sort_values(by="Count_AnimalName")
df = df.sort_values(by="Count_AnimalName", ascending=False)
# print(df)


# pandas取行或者列的注意事项
# - 方括号中写数组，表示取行，对行进行操作
# - 方括号中写字符串，表示取列索引，对列进行操作
print(df[:20])  # 取前20行内容
print(df["Row_Labels"])  # 取Row_Labels这一列的数据
print(df[:100]["Row_Labels"])  # 取前一百数据中的Row_Labels这列对应数据
print(" " * 50)
# pandas的布尔索引，&且 |或
# print(df[df["Count_AnimalName"] > 800])
# print(df[(df["Count_AnimalName"] > 800) & (df["Count_AnimalName"] < 1000)])
print(df[(df["Row_Labels"].str.len() > 4) & (df["Count_AnimalName"] > 700)])
