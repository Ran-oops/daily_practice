"""数组中的逆序对
描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P mod 1000000007
数据范围：  对于50% 的数据,size≤10^4
对于100% 的数据,size≤10^5
数组中所有数字的值满足0≤val≤10^9
要求：空间复杂度O(n)，时间复杂度O(nlogn)
输入描述：
题目保证输入的数组中没有的相同的数字
示例1
输入：
[1,2,3,4,5,6,7,0]
返回值：
7

示例2
输入：
[1,2,3]
返回值：
0
"""
from typing import List


def InversePairs1(nums: List[int]) -> int:
    """
    暴力破解法，时间复杂度是O(n²)
    5/6 组用例通过
    运行时间:6001ms
    占用内存:5632KB
    :param nums:
    :return:
    """
    ans = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i, n):
            if nums[i] > nums[j]:
                ans += 1

    return ans % 1000000007

print(InversePairs1([1,2,3,4,5,6,7,0]))


"""思路：
在归并排序的合并过程中，当左边的数组中的某个元素大于右边数组中的某个元素时，那么左边数组元素及其后面的所有元素都
可以与右边数组的当前元素构成逆序对。
 具体步骤：
 1. 使用归并排序递归地分割数组，直到每个子数组只有一个元素。
 2. 在合并两个有序子数组时，统计逆序对的数量。
 3. 逆序对的数量等于：当左边子数组的当前元素大于右边子数组的当前元素时，逆序对数量增加（mid - i + 1），其中mid是左边子数组的最后一个索引，i是左边子数组的当前指针。
 注意：需要将结果对1000000007取模。
 由于数组可能很大，递归深度可能较深，但题目要求空间复杂度O(n)，我们可以使用递归的归并排序，但也可以使用非递归版本以避免递归深度问题。不过Python的递归深度有限，对于10^5的数据可能会递归深度过大，因此我们可以使用迭代的归并排序（自底向上）来避免递归。
 但是，题目要求空间复杂度O(n)，所以我们需要在合并时使用额外的空间。

"""


class Solution:
    def __init__(self) -> None:
        # self.cnt = []
        self.cnt = 0

    def InversePairs(self, nums: List[int]) -> int:
        sorted_arr = self.merge_sort(arr=nums)
        print(f"sorted_arr: {sorted_arr}")
        # return sum(self.cnt) % 1000000007
        return self.cnt % 1000000007

    def merge_sort(self,arr):

        if len(arr) <= 1:
            return arr

        mid = (len(arr)) // 2
        left_sorted = self.merge_sort(arr[:mid])
        right_sorted = self.merge_sort(arr[mid:])
        sorted_arr = self.merge(left_sorted, right_sorted)

        return sorted_arr

    def merge(self, left, right):
        i = 0
        j = 0
        temp_list = []
        while i <= len(left) - 1 and j <= len(right) - 1:
            if left[i] <= right[j]:
                temp_list.append(left[i])
                i += 1
            else:
                temp_list.append(right[j])
                # self.cnt.append(len(left) - i)
                self.cnt += (len(left) - i)
                j += 1

        temp_list.extend(left[i:])
        temp_list.extend(right[j:])
        return temp_list












































