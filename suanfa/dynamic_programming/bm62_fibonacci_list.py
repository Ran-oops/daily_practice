



class Solution:
    """
    时间复杂度过高
    """
    def Fibonacci(self, n: int) -> int:
        # write code here
        if n <= 1:
            return n
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)


def fibonacci(n):
    """
    0 1 1 2
    :param n:
    :return:
    """
    if n<=1:
        return n

    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b

print(fibonacci(3))