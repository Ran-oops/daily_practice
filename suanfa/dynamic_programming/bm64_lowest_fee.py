"""BM64 最小花费爬楼梯

描述
给定一个整数数组 cost  ，其中
cost[i]  是从楼梯第i 个台阶向上爬需要支付的费用，下标从0开始。一旦你支付此费用，
即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
数据范围：数组长度满足 1≤n≤10^5，数组中的值满足 1≤cost i≤10^4

"""
from typing import List

def minCostClimbingStairs3(cost: List[int]) -> int:
    """
    我比较喜欢这个方式，容易理解，不绕
    注意：楼梯顶部在数组末尾之后，即需要到达第n个台阶（数组长度为n，则台阶索引为0到n-1，顶部是n）
    到达0台阶：花费0（因为我们选择从0开始，直接站在0上，但还没有支付0台阶的费用，当我们要从0往上跳的时候才支付0的费用）
    到达1台阶：花费0（同理）

    注意：我们最终要到达的是顶部，即第n个台阶（索引为n，但cost数组只有到n-1）。
    所以我们可以将dp数组长度设为n，然后最后一步可以从n-1或n-2直接跳到顶部（不需要支付顶部的费用，因为顶部没有cost）。
    最终的最小花费应该是 min(dp[n-1], dp[n-2])
    """
    # dp[i]表示爬到第i阶楼梯需要的最小花费
    dp = [0 for i in range(len(cost) + 1)]
    for i in range(2, len(cost) + 1):
        # 每次选取最小的方案
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    print(f"dp: {dp}")
    return dp[len(cost)]

print(minCostClimbingStairs3(cost=[2, 5, 20]))

def minCostClimbingStairs4(cost: List[int]) -> int:
    dp = [0 for i in range(len(cost)+1)]

    for y in range(2, len(dp)):
        dp[y] = min(dp[y-1]+cost[y-1], dp[y-2]+cost[y-2])

    print(f"dp44444: {dp}")
    return dp[-1]

print(minCostClimbingStairs4(cost=[2, 5, 20]))


def minCostClimbingStairs(cost):
    if len(cost)<=2:
        return min(cost)

    a, b = cost[0], cost[1]

    for i in range(2, len(cost)):
        next_cost = min(a, b) + cost[i]
        a, b = b, next_cost
    return min(a, b)



print(minCostClimbingStairs(cost=[2,5,20]))


def minCostClimbingStairs2(cost: List[int]) -> int:
    # 初始化前两个台阶的最小花费
    a, b = 0, 0

    # 动态规划：计算到达每个台阶的最小花费
    for c in cost:
        # 更新当前台阶的最小花费：前两个台阶的最小值 + 当前台阶花费
        a, b = b, min(a, b) + c

    # 最后一步可以从倒数第一或第二台阶直接到顶部
    return min(a, b)

print(minCostClimbingStairs2(cost=[2,5,20]))


















