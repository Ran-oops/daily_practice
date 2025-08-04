"""
42. 接雨水
已解答
困难
相关标签
premium lock icon
相关企业
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""

"""
解题思路：使用动态规划：
https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/
"""

def trap(height):
    res = 0
    n = len(height)
    pre_max = [0] * n
    sub_max = [0] * n
    pre_max[0] = height[0]
    sub_max[-1] = height[-1]
    for i in range(1,n):
        pre_max[i] = max(height[i], pre_max[i-1])

    for i in range(n-2, -1, -1):
        sub_max[i] = max(height[i], sub_max[i+1])

    print(f"pre_max: {pre_max}")
    print(f"sub_max: {sub_max}")

    for pre, sub, h in zip(pre_max, sub_max, height):
        res += min(pre, sub) - h
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
