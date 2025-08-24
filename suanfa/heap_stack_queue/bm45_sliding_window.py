"""
BM45 滑动窗口的最大值

描述
给定一个长度为 n 的数组 num 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。
窗口大于数组长度或窗口长度为0的时候，返回空。
数据范围： 1≤n≤10000
0≤size≤10000，数组中每个元素的值满足 ∣val∣≤10000∣val∣≤10000
要求：空间复杂度
O(n)，时间复杂度 O(n)

示例1
输入：
[2,3,4,2,6,2,5,1],3
复制
返回值：
[4,4,6,6,6,5]

"""
class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        # write code here
        if not num or size > len(num) or not size:
            return []
        res = []
        num_win = len(num) - size + 1
        for i in range(num_win):
            temp_list = num[i:i + size]
            res.append(max(temp_list))

        return res
























