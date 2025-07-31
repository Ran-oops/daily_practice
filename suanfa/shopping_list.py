def main():
    # 读取第一行的预算和物品总数
    first_line = input().split()
    n = int(first_line[0])
    m = int(first_line[1])
    n = n // 10  # 预算除以10（题目保证价格是10的倍数）

    items = []
    # 读取接下来的m行，每行包含v, w, q
    for _ in range(m):
        line = input().split()
        v = int(line[0])
        w = int(line[1])
        q = int(line[2])
        v = v // 10  # 价格除以10
        items.append((v, w, q))

    # 分离主件和附件
    main_items = [None] * m
    accessories = [[] for _ in range(m)]
    for idx in range(m):
        v, w, q = items[idx]
        if q == 0:
            main_items[idx] = (v, w)
        else:
            accessories[q - 1].append((v, w))  # 附件归属到对应主件（q-1是主件索引）

    print(f"main_items: {main_items}")
    print(f"accessories: {accessories}")
    # 生成每个主件组的所有可能组合
    groups = []
    for i in range(m):
        if main_items[i] is None:
            continue  # 跳过无效主件（如附件未被正确归类）
        v0, w0 = main_items[i]
        group = []
        # 1. 仅主件
        group.append((v0, v0 * w0))
        acc_list = accessories[i]
        # 2. 主件 + 附件1（如果存在）
        if len(acc_list) > 0:
            v1, w1 = acc_list[0]
            group.append((v0 + v1, v0 * w0 + v1 * w1))
            # 3. 主件 + 附件2（如果存在）
            if len(acc_list) > 1:
                v2, w2 = acc_list[1]
                group.append((v0 + v2, v0 * w0 + v2 * w2))
                # 4. 主件 + 附件1 + 附件2
                group.append((v0 + v1 + v2, v0 * w0 + v1 * w1 + v2 * w2))
        groups.append(group)

    # 初始化二维dp数组
    dp = [[0] * (n + 1) for _ in range(len(groups) + 1)]

    print(f"groups: {groups}")
    # 动态规划过程
    for i in range(1, len(groups) + 1):
        for j in range(n + 1):
            # 不选当前组
            dp[i][j] = dp[i - 1][j]
            # 尝试选当前组的每个组合
            for cost, value in groups[i - 1]:
                if j >= cost:
                    if dp[i - 1][j - cost] + value > dp[i][j]:
                        dp[i][j] = dp[i - 1][j - cost] + value

    # 输出最大满意度（恢复乘以10）
    # print(dp)
    print(dp[len(groups)][n] * 10)


if __name__ == "__main__":
    main()