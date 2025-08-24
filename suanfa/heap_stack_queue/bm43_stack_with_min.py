"""
BM43 包含min函数的栈
描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。

此栈包含的方法有：
push(value):将value压入栈中
pop():弹出栈顶元素
top():获取栈顶元素
min():获取栈中最小元素

数据范围：操作数量满足
0≤n≤300

0≤n≤300  ，输入的元素满足 ∣val∣≤10000

∣val∣≤10000
进阶：栈的各个操作的时间复杂度是 O(1)
空间复杂度是
O(n)

示例:
输入:    ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
输出:    -1,2,1,-1
解析:
"PSH-1"表示将-1压入栈中，栈中元素为-1
"PSH2"表示将2压入栈中，栈中元素为2，-1
“MIN”表示获取此时栈中最小元素==>返回-1
"TOP"表示获取栈顶元素==>返回2
"POP"表示弹出栈顶元素，弹出2，栈中元素为-1
"PSH1"表示将1压入栈中，栈中元素为1，-1
"TOP"表示获取栈顶元素==>返回1
“MIN”表示获取此时栈中最小元素==>返回-1

示例1
输入：
 ["PSH-1","PSH2","MIN","TOP","POP","PSH1","TOP","MIN"]
复制
返回值：
-1,2,1,-1

"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.stack_min:
            self.stack_min.append(node)
        else:
            if self.stack_min[-1] > node:
                self.stack_min.append(node)
            else:
                self.stack_min.append(self.stack_min[-1])

    def pop(self):
        # write code here
        self.stack.pop()
        self.stack_min.pop()

    def top(self):
        # write code here
        return self.stack[len(self.stack)-1]
    def min(self):
        # write code here
        return self.stack_min[-1]
























