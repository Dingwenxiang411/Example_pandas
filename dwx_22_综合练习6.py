import pandas as pd
import matplotlib.pyplot as plt
file_path = "./PM2.5/BeijingPM20100101_20151231.csv"
df = pd.read_csv(file_path)
# print(df.info())

# 把分开的时间字符串转换为pandas的时间类型
period_data = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
df["datatime"] = period_data

# 把datatime设置为索引
df.set_index("datatime", inplace=True)
print(df.head(3))

# 进行降采样，取每个月的平均值
df = df.resample("7D").mean()

# 处理缺失值，删除缺失数据
# dropna会删除所有含Nan的行，因为这里只有一列不同担心其他列的Nan对其影响
data = df["PM_US Post"].dropna()
data1 = df["PM_Dongsi"].dropna()

# 画图
_x = data.index
_y = data.values
_x_china = data1.index
_y_china = data1.values

# 数据缺失，造成中国和美国的数据不一致
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y, label="US_POST")
plt.plot(range(len(_x_china)), _y_china, label="CN_POST")
plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
# plt.xticks(list(range(len(_x_china)))[::10], list(_x_china)[::10])
plt.legend(loc="best")
plt.show()
