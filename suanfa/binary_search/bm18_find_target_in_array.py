"""BM18 二维数组中的查找
描述
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。
给定 target = 3，返回 false。
数据范围：矩阵的长宽满足 0≤n,m≤500， 矩阵中的值满足
0≤val≤10^9
进阶：空间复杂度O(1) ，时间复杂度O(n+m)
"""

"""
此题有两种解决方案，从矩阵的右上角或矩阵的左下角开始查找
以右上角为例：
    1.如果当前元素等于目标值，返回True
    2.如果当前元素大于目标值，那么目标值不可能在当前元素所在的列（因为当前列下边的元素都更大），所以排除当前列，向左移动
    3.如果当前元素小于目标值，那么目标值不可能在当前元素的所在的行(因为当前行左边的元素都更小),所以排除当前行，向下移动
    总结就是：只可以向左或向下移动
以左下角为例：
    1. 如果当前元素大于目标值，排除当前行，向上移动。
    2. 如果当前元素小于目标值，排除当前列，向右移动。
    总结就是：只可以向右或向上移动

"""

from typing import List


def Find1(self, target: int, array: List[List[int]]) -> bool:
    # write code here
    rows = len(array)
    if rows == 0:
        return False
    cols = len(array[0])
    if cols == 0:
        return False

    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

def Find(target: int, array: List[List[int]]) -> bool:
    i = len(array)
    if i == 0:
        return False
    j = len(array[0])
    if j == 0:
        return False

    r = i-1
    c = 0
    while r >= 0 and c < j:
        if array[r][c] == target:
            return True
        elif array[r][c] < target:
            c += 1
        else:
            r -= 1
    return False