"""
v<w(n), f(n,v) = f(n-1,v)
v>w(n), f(n,v) = max{f(n-1, v), f(n-1,v-w(n))+c(n)}
也就是说 当你考虑一个物品能不能加入背包时，需要这样判断：
1.若物品重量大于剩余的背包容量，那么就不能加入
2.若物品重量小于剩余的背包容量，那么可以根据max{不加入该物品的价值，加入该物品的价值+除去该物品的重量之外的最大价值}来进行判断需不需要加入
"""

weights = [3, 2, 4, 5, 1]
values = [50, 40, 70, 80, 10]
capacity = 7
dq = [[0]*(capacity+1)  for _ in range(len(weights)+1)]
for i in range(1, len(weights)+1):
    for j in range(1, capacity+1):
        if weights[i-1] > j:
            dq[i][j] = dq[i-1][j]
        else:
            dq[i][j] = max(
                dq[i-1][j],
                dq[i-1][j-weights[i-1]] + values[i-1]
            )


max_row_num = len(weights)
max_col_num = capacity
n = max_row_num
selected = []
w = capacity
for i in range(n, 0, -1):
    # 如果当前物品被选中(与上一行同容量的值不同)
    if dq[i][w] != dq[i-1][w]:
        selected.append(i-1)
        w -= weights[i-1]
for i in selected:
    print(f"{i}\t{weights[i]}\t{values[i]}")