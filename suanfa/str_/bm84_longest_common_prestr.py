"""BM84 最长公共前缀
给你一个大小为 n 的字符串数组 strs ，其中包含n个字符串 ,
编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀。
示例1
输入：
["abca","abc","abca","abc","abcc"]
返回值：
"abc"
"""
from typing import List


def longestCommonPrefix( strs: List[str]) -> str:
    # write code here
    res = ""
    if not strs:
        print(res)
        return res
    if any(len(item) == 0 for item in strs):
        print(res)
        return res
    min_str = min(strs, key=lambda x: len(x))

    for i in range(len(min_str)):
        tmp = min_str[:i + 1]
        if not all(item.startswith(tmp) for item in strs):
            break
        else:
            res = tmp
    print(res)
    return res
