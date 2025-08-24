def three_sum_zero(nums):
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


print(three_sum_zero([-1,0,1,2,-1,-4]))