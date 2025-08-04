"""
lc34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
# lower_bound 返回最小的满足 nums[i] >= target 的下标 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
def lower_bound(nums, target):
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        if nums[mid] >= target:
            right = mid  # 范围缩小到 (left, mid)
        else:
            left = mid  # 范围缩小到 (mid, right)
    # 循环结束后 left+1 = right
    # 此时 nums[left] < target 而 nums[right] >= target
    # 所以 right 就是第一个 >= target 的元素下标
    return right

def searchRange(nums, target):
    start = lower_bound(nums, target)  # 选择其中一种写法即可
    if start == len(nums) or nums[start] != target:
        return [-1, -1]  # nums 中没有 target
    # 如果 start 存在，那么 end 必定存在
    end = lower_bound(nums, target + 1) - 1
    return [start, end]




print(searchRange(nums = [5,7,7,8,8,10], target = 8))





