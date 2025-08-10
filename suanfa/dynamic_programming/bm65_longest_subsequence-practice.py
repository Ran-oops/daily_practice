"""BM65 最长公共子序列
描述
给定两个字符串str1和str2，输出两个字符串的最长公共子序列。如果最长公共子序列为空，则返回"-1"。目前给出的数据，仅仅会存在一个最长的公共子序列

数据范围：
0≤∣str1∣,∣str2∣≤2000
要求：空间复杂度
O(n^2) ，时间复杂度 O(n^2)
"""

"""
DP表结构
DP表是一个二维数组，大小为(m+1) x (n+1)，其中：

dp[i][j]表示字符串str1[0:i]和str2[0:j]的最长公共子序列长度
第0行和第0列初始化为0（空字符串与任何字符串的LCS长度为0）
DP表填充规则
如果当前字符相等：dp[i][j] = dp[i-1][j-1] + 1
如果当前字符不等：dp[i][j] = max(dp[i-1][j], dp[i][j-1])

示例2：str1 = "ABCD", str2 = "ACBD"
DP表：
  0  0  0  0  0
  0  1  1  1  1
  0  1  1  2  2
  0  1  2  2  2
  0  1  2  2  3

回溯过程
1.从DP表右下角dp[m][n]开始
2.如果当前字符相等：
    将该字符加入LCS
    向左上方移动（i--, j--）
3.如果当前字符不等：
    向dp值更大的方向移动（优先向上）
4.重复直到到达左上角
5.反转得到的序列即为LCS

复杂度分析
时间复杂度：O(m×n) - 填充DP表需要双重循环
空间复杂度：O(m×n) - DP表占用空间
"""


def LCS(str1, str2):
    m, n = len(str1), len(str2)
    # 创建(m+1)x(n+1)的DP表
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp)
    if dp[m][n] == 0:
        return -1

    i, j = m, n
    results = []
    while i>0 and j>0:
        if str1[i-1] ==  str2[j-1]:
            results.append(str1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1

    print(f"results: {results}")
    results.reverse()
    return "".join(results)




# 测试示例
if __name__ == "__main__":
    print(LCS("ABC", "AC"))  # 输出: "AC"
    print(LCS("ABCD", "ACBD"))  # 输出: 唯一解 (如题目保证)
    print(LCS("ABC", "DEF"))  # 输出: "-1"