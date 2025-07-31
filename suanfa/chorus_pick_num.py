# while True:
#     """
#     传统dp方法，时间复杂度是O(n²)
#     """
#     try:
#         num = input()
#         alist = list(map(int, input().strip().split(" ")))
#         lens = len(alist)
#         left_smaller, right_smaller = [1] * lens, [1] * lens
#         for i in range(lens):
#             for j in range(i):
#                 if alist[j] < alist[i]:
#                     left_smaller[i] = max(left_smaller[j] + 1, left_smaller[i])
#
#         for i in range(lens - 1, -1, -1):
#             for j in range(lens - 1, i, -1):
#                 if alist[j] < alist[i]:
#                     right_smaller[i] = max(right_smaller[j] + 1, right_smaller[i])
#
#         new_alist = list(map(lambda a, b: a + b -1, left_smaller, right_smaller))
#         max_num = max(new_alist)
#         pick_num = lens - max_num
#         print(pick_num)
#
#     except:
#         break

import bisect

count = 0
def compute_lis(arr):
    tails = []
    res = [1] * len(arr)
    for i in range(len(arr)):
        idx = bisect.bisect_left(tails, arr[i])
        if idx == len(tails):
            tails.append(arr[i])
        else:
            tails[idx] = arr[i]
        res[i] = idx + 1
    return res


while count<1:
    try:
        _ = 8  # 读取但不使用第一行的数字
        # alist = list(map(int, input().strip().split()))
        astr = "186 186 150 200 160 130 197 200"
        alist = list(map(int, astr.strip().split()))
        lens = len(alist)

        # 计算从左到右的最长严格递增子序列
        left = compute_lis(alist)
        # 计算从右到左的最长严格递减子序列
        right = compute_lis(alist[::-1])
        right = right[::-1]

        print(left)
        # 计算每个位置作为山顶时的最长合唱队形
        max_len = 1  # 至少可以保留1人
        for i in range(lens):
            if left[i] > 1 and right[i] > 1:  # 确保有递增和递减部分
                max_len = max(max_len, left[i] + right[i] - 1)

        print(lens - max_len)
        count += 1
    except:
        break




















