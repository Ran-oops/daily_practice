"""BM83 字符串变形
描述
对于一个长度为 n 字符串，我们需要对它做一些变形。
首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把这个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。
比如"Hello World"变形后就变成了"wORLD hELLO"。
"""

"""
astr.swapcase()是将字符串里面的字母大写变小写，小写变大写
"""

class Solution:
    def trans(self , s, n):
        # write code here
        split_s = s.split(" ")
        split_s.reverse()
        for i in range(len(split_s)):
            split_s[i] = split_s[i].swapcase()
        return " ".join(split_s)