"""BM66 最长公共子串
描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。

数据范围：
1≤∣str1∣,∣str2∣≤5000
要求： 空间复杂度 O(n^2)
"""

"""动态规划逻辑
dp[i][j] = dp[i-1][j-1] + 1
if dp[i][j] > max_len:
    max_len = dp[i][j]
    end_pos = i-1
"""
def LCS1(str1, str2):
    """
    时间复杂度较高， 有一个用例因为超时而没有通过

    以i位置的字母为开头
    """
    if len(str2) < len(str1):
        str1, str2 = str2, str1
    res_list = []
    for i in range(len(str1)):
        right = i+ 1
        res = ""
        while str1[i: right] in str2 and right <= len(str1):
            res = str1[i: right]
            right += 1

        res_list.append(res)
    return  max(res_list, key=len)

print(LCS1("1AB2345CD","12345EF"))
print(LCS1("1B23D","123F"))

def LCS2(str1, str2):
    """
    时间复杂度也高，有三个用例没有通过
    """
    m, n = len(str1), len(str2)

    dp = [[0] * (n+1) for _ in range(m+1)]
    max_len = 0
    end_pos = -1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i-1

    return str1[end_pos-max_len+1: end_pos+1]

print("LCS2==========")
print(LCS2("1AB2345CD","12345EF"))
print(LCS2("1B23D", "123F"))


def LCS3(str1, str2):
    """
    时间复杂度也高，有三个用例没有通过
    这个是使用滚动数组来优化空间复杂度的
    为什么能压缩为一维数组？
        计算当前行 dp[i][j]只需要：
        上一行 dp[i-1][j-1]（左上角值）
        不需要整行或整列数据
    为什么从后向前更新？
        从后向前更新，不会破坏需要的数据
    """
    m, n = len(str1), len(str2)

    dp = [0] * (n+1)
    max_len = 0
    end_pos = 0
    for i in range(1, m+1):
        for j in range(n, 0, -1):
            if str1[i-1] == str2[j-1]:
                dp[j] = dp[j-1] + 1
                if dp[j] > max_len:
                    max_len = dp[j]
                    end_pos = i-1
            else:
                dp[j] = 0
    return str1[end_pos-max_len+1: end_pos+1]

print("LCS3==========")
print(LCS3("1AB2345CD","12345EF"))
print(LCS3("1B23D", "123F"))


def LCS4(str1: str, str2: str) -> str:
    # 让str1为较长的字符串
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    res = ''
    max_len = 0
    # 遍历str1的长度
    for i in range(len(str1)):
        # 查找是否存在
        if str1[i - max_len: i + 1] in str2:
            res = str1[i - max_len: i + 1]
            max_len += 1
    return res


print("LCS4==========")
print(LCS4("1AB2345CD","12345EF"))
print(LCS4("1B23D", "123F"))
print(LCS4("abcbcde", "bbcd"))


def LCS5(str1, str2):

    """

    0 1 2 3

    i = 1
    max_lens = 1
    str1[0:2]  01

    i=2
    max_lens=1
    str1[1:3] 12

    通过了所有测试用例

    以i位置的字母为结尾
    其实本质上也是滑动窗口
    """
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    max_lens = 0
    res = ""
    for i in range(len(str1)):
        if str1[i-max_lens: i+1] in str2:
            res = str1[i-max_lens: i+1]
            max_lens += 1

    return res


print("LCS5==========")
print(LCS5("1AB2345CD","12345EF"))
print(LCS5("1B23D", "123F"))
print(LCS5("abcbcde", "bbcd"))



def LCS6(str1, str2):
    """
    使用滑动窗口实现
    """
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    left = 0
    res = ""
    for i, v in enumerate(str1):
        if str1[left: i+1] in str2:
            res = str1[left: i+1]
        else:
            left += 1
    return  res

print("LCS6==========")
print(LCS6("1AB2345CD","12345EF"))
print(LCS6("1B23D", "123F"))
print(LCS6("abcbcde", "bbcd"))
print(LCS6("abc", "def"))















