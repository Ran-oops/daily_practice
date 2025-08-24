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


def merge_sort_iterative(arr):
    """
    使用迭代方法实现归并排序

    参数:
    arr: 待排序的列表

    返回:
    排序后的列表
    """
    n = len(arr)
    # 如果数组长度为0或1，直接返回
    if n <= 1:
        return arr

    # 创建临时数组用于归并操作
    temp = [0] * n
    size = 1  # 当前归并的子数组大小

    # 外层循环：不断增大归并的子数组大小
    while size < n:
        # 内层循环：遍历所有需要归并的子数组对
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)  # 计算中间位置
            right = min(left + 2 * size, n)  # 计算右边界

            # 合并两个有序子数组 [left, mid) 和 [mid, right)
            i, j, k = left, mid, left

            # 将两个子数组中的较小元素依次放入临时数组
            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1

                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            # 将剩余元素复制到临时数组
            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # 将临时数组中的元素复制回原数组
            for k in range(left, right):
                arr[k] = temp[k]

        # 增大子数组大小
        size *= 2

    return arr


# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]

    for i, arr in enumerate(test_cases):
        print(f"测试用例 {i + 1}: {arr}")
        sorted_arr = merge_sort_iterative(arr.copy())
        print(f"排序结果: {sorted_arr}\n")










































