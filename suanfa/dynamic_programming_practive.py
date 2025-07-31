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
r, c = len(weights) + 1, capacity + 1
dp = [[0]*c for _ in range(r)]

for i in range(1, r):
    for j in range(1, c):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-weights[i-1]] + values[i-1]
            )
print(dp)

selected = []
w = capacity
for k in range(len(weights), 0, -1):
    if dp[k][w] != dp[k-1][w]:
        selected.append(k-1)
        w = w - weights[k-1]

for m in selected:
    print(f"{weights[m], values[m]}")

