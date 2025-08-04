
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    单链表实现
    """
    def __init__(self):
        self.head = None
        self.size = 0


    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def reverseBetween(self, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = self.head
        pre = dummy

        # 移动prev到反转区间的前一个节点：
        for _ in range(m-1):
            pre = pre.next

        # 初始话反转区间起点
        cur = pre.next
        prev_node = None

        for _ in range(n-m+1):
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
        pre.next.next = cur
        pre.next = prev_node

        return dummy.next



    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")

        if index == 0:
            self.prepend(value)
            return

        new_node = ListNode(value)
        current = self.head
        for _ in range(index-1):
            current = current.next # 找到头一个节点

        new_node.next = current.next
        current.next = new_node
        self.size += 1


    def remove(self, value):
        """删除包含指定值的节点"""
        if self.head is None:
            raise ValueError("List is empty")

        while self.head and self.head.value == value:
            self.head = self.head.next
            self.size -= 1

        current = self.head
        while current.next:
            if current.next.value == value: # 找到值等于target的下一个节点
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def search(self, value):
        """检查节点是否存在"""
        current = self.head
        while current.next:
            if current.value == value:
                return True
            current = current.next

        return False

    def reverse(self):
        """反转链表"""
        prev = None
        current = self.head
        while current:
            next_node = current.next # 存next
            current.next = prev  # 改next
            prev = current  # 改prev
            current = next_node # 改current

        self.head = prev



    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                cur = cur.next
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
                cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2

        return dummy.next




ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
# print(ll.head.next.value)
# print(ll.size)

# ll.reverse()
# print(ll.head.value)
# print(ll.size)
# print(ll.search(5))

ll.reverseBetween(2,4)
print(ll.head.value)
print(ll.head.next.value)
print(ll.head.next.next.value)
print(ll.head.next.next.next.value)
print(ll.head.next.next.next.next.value)







































