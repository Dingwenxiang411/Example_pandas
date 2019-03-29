max_num = 9.1
min_num = 1.6
num_list = []
while min_num <= max_num:
    num_list.append(min_num)
    min_num += 0.5

print(num_list)

a = [1.6]
for i in range(1, 16):
    a += [1.6 + i * 0.5]

print(a)
