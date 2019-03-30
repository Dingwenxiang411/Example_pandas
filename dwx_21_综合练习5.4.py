import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 统计不同月份不同类型的电话次数的变化情况

file_path = "./911.csv"
df = pd.read_csv(file_path)
# 将df中的timeStamp数据转换成pandas能识别的时间序列
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

# 添加列，表示分类
temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
# 要给一个DataFrame插入数据，直接指定新的索引名就可以了
df["cate"] = cate_df
# inplace的作用就是实现对原始数据的修改，因为作用函数本身没有返回值
# 如果放在前面空的那一行，会造成索引改变，cate_df全为nan，因为pd.DataFrame只能索引0、1、2、3
df.set_index("timeStamp", inplace=True)
print(df.head())

# 分组
for group_name, group_data in df.groupby(by="cate"):
    # groupby之后是一个元祖
    # 对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]
    _x = count_by_month.index
    _y = count_by_month.values
    # 将时间格式化，不然含有小时分钟
    _x = [i.strftime("%Y-%m-%d") for i in _x]
    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
