
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

nums = [5, 4, 3, 2, 1]
print(f"原始序列：{nums}")
print(f"排序后的序列：{bubble_sort(nums)}")