import pandas as pd

a = pd.DataFrame({"a": range(7), "b": range(7, 0, -1), "c": ["one", "one", "one", "two", "two", "two", "two"],
                  "d": list("hjklmno")})
print(a)
b = a.set_index(["c", "d"])
print(b)
# 下面这种方式属于按列取元素，而不是索引
c = b["a"]
print(c)
# 提取h处的数据，loc按索引取数据
print(c.loc["one"].loc["h"])
print("*" * 50)
print(c.swaplevel().loc["h"])
# 以上两种方法都可以取到"h"的数据，swaplevel反转一下索引
