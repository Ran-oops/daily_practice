"""BM19 寻找峰值
描述
给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
2.假设 nums[-1] = nums[n] =−∞
3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
4.你可以使用O(logN)的时间复杂度实现此问题吗？

数据范围：1≤nums.length≤2×10^5
−2^31<=nums[i]<=2^31 −1

如输入[2,4,1,2,7,8,4]时，会形成两个山峰，一个是索引为1，峰值为4的山峰，另一个是索引为5，峰值为8的山峰，如下图所示：

"""
from typing import List


def findPeakElement1(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if nums[1] < nums[0]:
        return 0
    if nums[-2] < nums[-1]:
        return n - 1

    for i in range(1, n - 2):
        if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
            return i

def findPeakElement2(nums: List[int]) -> int:
    # write code here
    n = len(nums)
    left = 0
    right = n-1
    while left < right:  # 当left == right时循环结束
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid +1  # 相当于每次的left或right都赋值为较大数的那个index
        else:
            right = mid
    return left  # 当left == right时循环结束，因此return left还是return right都一样

print(findPeakElement2([2,4,1,2,7,8,4]))

