"""
209. 长度最小的子数组
中等
相关标签
premium lock icon
相关企业
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：
输入：target = 4, nums = [1,4,4]
输出：1
示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""

def minSubArrayLen(target, nums):
    """
    时间复杂度O(n²), 超时了
    :param target:
    :param nums:
    :return:
    """
    res = len(nums)
    if sum(nums)< target:
        return 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] >= target:
            res = 1
        suma = nums[i]
        j = i-1
        suma += nums[j]
        a = 2
        while suma < target and j > 0:
            a+=1
            j -= 1
            suma += nums[j]
            if a > res:
                break
        if suma >= target:
            res = min(res, a)

    return res

# print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
# print(minSubArrayLen(target = 4, nums = [1,4,4]))
# print(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen(target = 15, nums = [1,2,3,4,5]))

def minSubArrayLen2(target, nums):
    n = len(nums)
    res = n + 1
    t = 0
    s = 0
    for i, x in enumerate(nums):
        t += x
        while t >= target:
            res = min(res, i- s + 1)
            t -= nums[s]
            s += 1
    return res if res <= n else 0

print(minSubArrayLen2(target = 15, nums = [1,2,3,4,5]))



















