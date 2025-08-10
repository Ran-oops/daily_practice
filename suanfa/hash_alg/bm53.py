"""BM53 缺失的第一个正整数
描述
给定一个无重复元素的整数数组nums，请你找出其中没有出现的最小的正整数

进阶： 空间复杂度 O(1）
时间复杂度 O(n）

数据范围:
−2^31≤nums[i]≤2^31−1
0≤len(nums)≤5∗10^5
"""

"""
特别注意：这里用了set()集合，将list转换为set, 因为查找元素 (x in container)时：
原理：

List：顺序存储，必须遍历所有元素，时间复杂度为O(n)
Set：基于哈希表实现，通过哈希函数直接计算存储位置O(1)
"""

class Solution:
    def minNumberDisappeared(self , nums: List[int]) -> int:
        # write code here
        nums = set(nums)
        n = len(nums)
        for i in range(1, n+2):
            if i not in nums:
                return i




