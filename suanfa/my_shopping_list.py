import collections
fir_str = input().strip().split()
yusuan = int(fir_str[0]) // 10
all_num = int(fir_str[1])


ac = []
all_items = []
acc_li = []
adict = collections.defaultdict(list)
for i in range(all_num):
    each_str = list(map(int, input().strip().split()))
    if each_str[2] != 0:
        each_str[2] = each_str[2] - 1
        # ac.append([i, each_str[2]])
        adict[each_str[2]].append(i)
        acc_li.append(each_str[2])
    all_items.append(each_str)

# print(adict)
# print(list(set(acc_li)))
# print(all_items)

calculated_items = []
for j in list(set(acc_li)):
    main_one = all_items[j]
    if len(adict[j]) == 1:
        # 只有两种情况：
        # 1. 只拿主件
        # 2. 拿主件加附件
        fu_item = all_items[adict[j][0]]
        calculated_items.append(((main_one[0]+fu_item[0])//10, (main_one[0]*main_one[1]+fu_item[0]*fu_item[1])// 10))
    else:
        # 有四种情况，1.主件 2.主件+附件一  3，主件+附件二  4. 主件+附件一+附件二
        fu1 = all_items[adict[j][0]]
        fu2 = all_items[adict[j][1]]
        calculated_items.append(((main_one[0]+fu1[0])// 10, (main_one[0]*main_one[1]+fu1[0]*fu1[1])// 10))
        calculated_items.append(((main_one[0]+fu2[0])// 10, (main_one[0]*main_one[1]+fu2[0]*fu2[1])// 10))
        calculated_items.append(((main_one[0]+fu2[0]+fu1[0])//10, (main_one[0]*main_one[1]+fu2[0]*fu2[1]+fu1[0]*fu1[1])// 10))


for i in list(set(acc_li)):
    an_item = all_items.pop(i)
    calculated_items.insert(0, [int(an_item[0])// 10, int(an_item[1])])
valid_items = [(int(i[0])//10, int(i[1])) for i in all_items if i[2]==0]
# valid_items += calculated_items
print(calculated_items)

valid_items = valid_items + calculated_items
# print(valid_items)
# valid_items = [
#     [(1,3)],
#     [(1,2)],
#     [(1,1), (3,7), (3,7), (5,13)]
# ]
# dp = [[0] * (yusuan+1) for _ in range(len(valid_items)+1)]
# for i in range(1, len(valid_items) + 1):
#     for j in range(yusuan+1):
#         dp[i][j] = dp[i - 1][j]
#         for k in calculated_items:
#             if j >= k[0]:
#                 # dp[i][j] = max(
#                 #     dp[i-1][j],
#                 #     dp[i-1][j-k[0]] + k[1]
#                 # )
#                 if dp[i - 1][j - k[0]] + k[1] > dp[i][j]:
#                     dp[i][j] = dp[i - 1][j - k[0]] + k[1]


# valid_items = [
#     (1,3),
#     (1,2),
#     (3,7), (3,7), (5,13), (1,1)
# ]
dp = [[0] * (yusuan+1) for _ in range(len(valid_items)+1)]
# for i in range(1, len(valid_items) + 1):
#     for j in range(1, yusuan+1):
#         dp[i][j] = dp[i - 1][j]
#
#         if j >= valid_items[i-1][0]:
#             dp[i][j] = max(
#                 dp[i-1][j],
#                 dp[i-1][j-valid_items[i-1][0]] + valid_items[i-1][1]
#             )


for i in range(1, len(valid_items) + 1):
    for j in range(1, yusuan+1):
        if int(valid_items[i - 1][0]) > int(j):
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-valid_items[i-1][0]] + valid_items[i-1][1]
            )
print(dp[len(valid_items)][yusuan] * 10)

# print(dp)


