"""
BM44 有效括号序列
题目
栈
字符串
描述
给出一个仅包含字符仅由括号字符
‘[’ ‘]’、‘(’、‘)’、‘{’、‘}’ 的括号序列字符串
s（0≦∣s∣≦1040≦∣s∣≦104），你需要判断给出的括号序列字符串s 是否是有效的括号序列。

示例1
输入："["
返回值：false
"""

class Solution1:
    def isValid(self , s: str) -> bool:
        # write code here
        if len(s) % 2 != 0:
            return False
        if not s:
            return True

        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if not s:
            return True
        else:
            return False



class Solution2:
    def isValid(self , s: str) -> bool:
        # write code here
        astack = []
        adict = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in list('({['):
                astack.append(i)
            else:
                if astack and i == adict[astack[-1]]:
                    astack.pop()
                else:
                    return False

        return astack == []

















