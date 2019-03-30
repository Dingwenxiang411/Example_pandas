import pandas as pd

print(pd.date_range(start="20181201", end="20190131", freq="D"))
print(pd.date_range(start="20181201", end="20190131", freq="10D"))
print(pd.date_range(start="20181201", periods=10, freq="D"))
print(pd.date_range(start="20181201", periods=10, freq="M"))
