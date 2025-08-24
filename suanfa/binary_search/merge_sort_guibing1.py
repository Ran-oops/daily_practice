"""merge sort 归并排序的python实现
归并排序是一种高效的分治算法，其核心思想是将数组分成两半，分别排序，然后将两个有序的子数组合并成一个
有序数组

算法步骤
1.分解：将当前数组分成两个子数组
2.解决：递归地对两个子数组进行排序
3.合并：将两个已排序的子数组合并成一个有序数组

优化方向：
1.对于小数组可以使用插入排序来提高性能
2.如果已经有序，可以跳过合并步骤
3.使用迭代而非递归的实现可以减少函数调用开销
归并排序是稳定且高效的排序算法，特别适合处理大规模数据和外排序场景
"""

cnt = []
def merge_sort(arr):
    """
    归并排序主函数
    """
    # 递归终止条件：数组长度为1或0
    if len(arr) <= 1:
        return arr

    # 1. 分解：找到中间点，分割数组
    mid = len(arr) // 2
    # 2. 解决：递归排序左右子数组
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    # 3. 合并：合并两个已排序的子数组
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    合并两个已排序的数组
    """
    result = []  # 存放合并结果的数组
    i = j = 0  # 初始化左右数组的指针

    # 比较两个数组的元素，将较小的元素添加到结果中
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            cnt.append(len(left) - i)
            j += 1

    # 将剩余元素添加到结果中
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 测试代码
if __name__ == "__main__":
    # 示例
    arr = [1,2,3,4,5,6,7,0]
    print("原始数组:", arr)

    sorted_arr = merge_sort(arr)
    print("排序后数组:", sorted_arr)

    print("最终交换的次数", sum(cnt))









































