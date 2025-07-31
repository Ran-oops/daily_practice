

# num = int(input())
# alist = []
# adict = {}
# for i in range(num):
#     new_str = input()
#     new_alist = new_str.split()
#     if adict.get(int(new_alist[0]),None):
#         adict[int(new_alist[0])].append(int(new_alist[1]))
#     else:
#         adict[int(new_alist[0])] = [int(new_alist[1])]
#
#
# aorted_dict = dict(sorted(adict.items(), key=lambda x: x[0]))
# for x, y in aorted_dict.items():
#     print(x, sum(y))

# astr = "9876673"
# averted_str = astr[::-1]
# final_str = ""
# for i in averted_str:
#     if i not in final_str:
#         final_str += i
# print(final_str)


# line = "[@A8aA].0"
# indexes = set()
# for i in line:
#     if 0 <= ord(i) <= 127:
#         print(f"i: ord(i)=={i}:{ord(i)}")
#         indexes.add(i)
# print(len(indexes))


# alist = input().split(";")
# alist = [i for i in alist if i]
# valid_list = [[i[0], i[1:]] for i in alist if len(i)>2 and i[0] in ['A', 'D', 'W', 'S']]
#
# x,y = 0,0
# for i in alist:
#     if i[0] in list('ADWS'):
#         if i[1:].isdigit() and 0<int(i[1:])<100:
#             if i[0] == 'A':
#                 x -= int(i[1:])
#             elif i[0] == 'D':
#                 x += int(i[1:])
#             elif i[0] == 'W':
#                 y += int(i[1:])
#             else:
#                 y -= int(i[1:])
#
#
# print(f"{x},{y}")


import sys
import collections
import functools

##################################################
# （1）获取输入
n, m = map(int, input().strip().split())
v = [0] * m  # 重复操作符（价格）
p = [0] * m  # 重复操作符（满意度）
q = [0] * m  # 重复操作符（主件、附件编号）
##################################################
# （2）获取附件的编号
d = collections.defaultdict(list)#储存主件和对应的附件
# collections.defaultdict(default_factory):如果该变量存在，则初始化；如果没有，则为None。其他功能与dict相同。
# 使用list作为参数，可以将键值对序列转换为列表字典。
for i in range(m):  # 遍历所有件（包括：主件、附件）
    temm = list(map(int, input().strip().split()))  # 获取输入
    v[i], p[i], q[i] = temm[0], temm[1], temm[2] - 1  # 获取价格、重要度、主附件编号（编号减一，因为索引从0开始）
    if q[i] != -1:  # -1：表示主件（因为主件为0-1）	其余值：表示附件
        d[q[i]].append(i)  # 保存所有附件物品的编号（在多个附件中，将相同主件编号的附件存放在一个value中）
        #这里就是用默认的原因了，如果不存在直接创建而不会报错
##################################################
# （3）保存各种组合的价格、满意度
dn = collections.defaultdict(list)
for k in d.keys():  # 遍历字典key
    dn[k].append([v[k], v[k] * p[k]])  # 保存（附件）价格、满意度
    for i in d[k]:  # 遍历字典key对应的value（列表类型）
        # cc1 = v[k]						# key值对应的附件
        # cc2 = v[i]						# key对应的value值的附件
        dn[k].append([v[i] + v[k], v[i] * p[i] + v[k] * p[k]])  # 保存（两两附件）的价格、满意度

    if len(d[k]) == 2:  # 若key对应的value有两个（列表类型）
        # 每个主件可以有0个、1个、2个附件，附件不再有从属于自己的附件。
        # c1 = v[d[k][0]]				# key值对应的附件
        # c2 = v[i]						# key对应的value值的附件
        # c3 = v[d[k][1]]				# key对应的value值的附件
        dn[k].append(
            [
                v[d[k][0]] + v[k] + v[d[k][1]],  # 保存（三个附件）的价格、满意度
                v[d[k][0]] * p[d[k][0]] + v[k] * p[k] + v[d[k][1]] * p[d[k][1]],
            ]
        )

for i in range(m):
    if i not in d and q[i] == -1:
        dn[i].append([v[i], v[i] * p[i]])  # 保存（主件）的价格、满意度

##################################################
# （4）打印输出
@functools.cache
def f(i, n):
    if n < 0:
        return 0
    if i < 0:
        return 0
    res = f(i - 1, n)  # 递归循环（初始化为0）

    for v, vp in dn[k[i]]:  # 遍历key对应的多个value，获取对应的价格、满意度
        if v > n:
            continue  # 若价格大于总额，舍弃
        res = max(res, f(i - 1, n - v) + vp)  # 递归循环（遍历所有满足条件的附件，并获取最大满意度）
    return res


k = list(dn.keys())  # 获取字典的key值，并转换为列表类型
print(f(len(k) - 1, n))

























