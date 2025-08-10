def bubble_sort(arr):
    """
    冒泡排序算法实现（升序排序）

    参数:
    arr -- 待排序的列表

    返回:
    排序后的列表
    """
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        # 标记：用于优化（如果某轮没有交换，说明已排序完成）
        swapped = False

        # 最后 i 个元素已经排好序，无需再比较
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 如果本轮没有发生交换，说明数组已完全排序
        if not swapped:
            break

    return arr


# 测试示例
if __name__ == "__main__":
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", test_data)

    # 调用冒泡排序
    sorted_data = bubble_sort(test_data)
    print("排序后:", sorted_data)