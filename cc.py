"""
统计列表中元素频率
使用列表推导式查找列表中的重复元素
lamda查找字典value==3的键值对
找列表第二大元素
两个字典合并
不用使用循环反转字符串
"""
# 1. count

alist = [1,2,2, 3,5,4,4,3]
aset = list(set(alist))
count_dict = {}
for i in aset:
    count_dict[i] = alist.count(i)
print(count_dict)

# 2.find duplicated item
duplicated_item = [j for j in aset if alist.count(j)>1]
print(duplicated_item)

# 3. value=3
new_dict = {"name":"xx", "age":3}
print({k: v for k, v in new_dict.items() if v == 3})
print("==========")
print(dict(filter(lambda k:k[1]==3, new_dict.items())))
print("==========")

# 2nd largest
new_list = [1,2,2,3,5,4,4,3]
def bubble_sort(a_list):
    length = len(new_list)

    for i in range(length-1):
        for j in range(i+1, length-1):
            if a_list[j] > a_list[j+1]:
                a_list[j], alist[j+1] = a_list[j+1], alist[j]

    return a_list

print(bubble_sort(new_list))
second_l_v = list(set(bubble_sort(new_list)))[-2]
print(second_l_v)

# 5.union two dicts
f_dict = {"name":11, "age":25}
s_dict = {"major":22, "name": 22}
unioned_first_dict = (f_dict | s_dict)
print(f_dict.keys())
for i in f_dict.keys():
    if i in s_dict.keys():
        unioned_first_dict[i]+= f_dict[i]
print(unioned_first_dict)

a_str = "hello"
print(a_str[::-1])

















