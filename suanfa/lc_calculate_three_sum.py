"""
LC15. 三数之和
已解答
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

"""

def threeSum(nums):
    ans = []
    nums.sort()
    print(nums)
    n = len(nums)
    if nums[0]>0:
        return []
    if len(nums)<3:
        return []

    for i in range(n-2):
        # range(n-2) 明确表示"只需要遍历到倒数第三个元素"
        if nums[i]>0:
            return ans
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while(j<k):
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])
                while j<k and nums[j]== nums[j+1]:
                    j +=1
                while j<k and nums[k] == nums[k-1]:
                    k -=1
                j += 1
                k -= 1

            elif nums[i] + nums[j] + nums[k] > 0:
                k -=1
            else:
                j += 1
    return ans


print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,0,0]))

"""
为什么是 j += 1 和 k -= 1，而不是只移动一个？
因为：
如果只移动 j（j += 1），那么 nums[i] + nums[j] + nums[k] 可能会 变大（因为数组已排序，nums[j+1] >= nums[j]），导致错过可能的解。
如果只移动 k（k -= 1），那么 nums[i] + nums[j] + nums[k] 可能会 变小（因为 nums[k-1] <= nums[k]），同样可能错过解。
同时移动 j 和 k 可以 高效地探索所有可能的组合，避免重复计算。
"""

