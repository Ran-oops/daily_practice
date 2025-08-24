cnt = []
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = (len(arr)) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    sorted_arr = merge(left_sorted, right_sorted, cnt)

    return sorted_arr

def merge(left, right, cnt):
    i = 0
    j = 0
    temp_list = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp_list.append(left[i])
            i+=1
        else:
            temp_list.append(right[j])
            cnt.append(len(left)-i)
            j+= 1


    temp_list.extend(left[i:])
    temp_list.extend(right[j:])
    return temp_list



if __name__ == "__main__":
    # 示例
    arr = [1,2,3,4,5,6,7,0]
    print("原始数组:", arr)

    sorted_arr = merge_sort(arr)
    print("排序后数组:", sorted_arr)

    print("最终交换的次数", sum(cnt))


