def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = (len(nums)) // 2
    left_sort = merge_sort(nums[:mid])
    right_sort = merge_sort(nums[mid:])
    return merge(left_sort, right_sort)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left)  and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


nums = [5, 4, 3, 2, 1]
print(f"原始序列：{nums}")
print(f"排序后的序列：{merge_sort(nums)}")


