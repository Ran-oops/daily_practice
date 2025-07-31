
def knapsack_01(weights, values, capacity):
    """
    使用动态规划解决01背包问题(含最优解物品选择)
    :param weights(list): 物品重量列表，例如[3,2,4,5,1]
    :param values(list): 物品价值列表，例如[50,40,70,80,10]
    :param capacity(int): 背包最大容量，例如7
    :return:
        list: 动态规划表格(二维列表)
        int： 可获得的最大价值
        list: 被选中的物品索引列表(从0开始)
    """
    n = len(weights)
    # 初始化DP表格(n+1)行x（capacity+1）列
    dp = [[0] * (capacity + 1) for _ in  range(n+1)]
    # 填充dp表格
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:

                dp[i][w] = max(values[i-1]+ dp[i-1][w-weights[i-1]],
                dp[i-1][w]
              )
            else:
                dp[i][w] = dp[i-1][w]

    # 回溯找出被选中的物品
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        # 如果当前物品被选中(与上一行同容量的值不同)
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]

    return dp, dp[n][capacity], selected

def print_solution(weights, values, selected, max_value):
    """打印最优详情信息"""
    print(f"总价值：{max_value}")
    print(f"总重量： {sum(weights[i] for i in selected)}")
    print("被选中的物品：")
    print("索引\t重量\t价值")
    for i in selected:
        print(f"{i}\t{weights[i]}\t{values[i]}")


weights = [3, 2, 4, 5, 1]
values = [50, 40, 70, 80, 10]
capacity = 7

# 解决问题
dp_table, max_value, selected_items = knapsack_01(weights, values, capacity)
print("动态规划表格：")
print("  " + " ".join(f"{w:3}" for w in range(capacity +  1)))
for i, row in enumerate(dp_table):
    print(f"{i:2} " + " ".join(f"{v:3}" for v in row))

#打印最优解
print_solution(weights,values,selected_items, max_value)
