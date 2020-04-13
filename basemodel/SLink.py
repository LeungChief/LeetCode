class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{}'.format(self.val)


# 单向链表
class SLink(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    # 尾部追加
    def append(self, item, self_inc=True) -> object:

        node = ListNode(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        if self_inc:
            self.__size += 1

        return self

    # 指定位置前插入
    def add(self, offset, item) -> object:
        if offset < 0: raise IndexError

        for i, node in enumerate(self.iternodes()):
            if i == offset:
                cur = node
                break
        else:
            raise IndexError
        pre = self.__find_pre__(cur)
        node = ListNode(item)  # 新的节点
        if cur == self.head:  # 头部位置前插入
            self.head = node  # 当前头部等于当前创建的节点
            self.head.next = pre  # 下一个节点指向原来头部的下一个节点

        else:  # 其他位置前插入
            node.next = pre.next  # 与指定位置创建向下指针
            pre.next = node  # 指定节点的前一个节点的指针改为指向当前创建的节点

        return self

    # 指定位置后插入
    def insert(self, offset, item) -> object:

        if offset < 0:
            raise IndexError

        for i, node in enumerate(self.iternodes()):
            if i == offset:
                cur = node
                break
        else:
            raise IndexError

        newNode = ListNode(item)

        if cur is self.tail:
            self.append(item, False)
        else:
            newNode.next = cur.next
            cur.next = newNode

        self.__size += 1

        return self

    # 移除指定位置  (除头尾外位置时间复杂度 O(n2)>time>O(n) 头尾位置O(n)>time>O(1))
    def removeOffset(self, offset, left=False, right=False) -> object:

        if offset < 0: raise IndexError

        for i, node in enumerate(self.iternodes()):
            if i == offset:
                cur = node
                break
        else:
            raise IndexError

        if cur is self.head:  # 删除的节点是头
            self.head = cur.next
        elif cur is self.tail:  # 删除的节点是尾
            pre = self.__find_pre__(cur)
            pre.next = None
            self.tail = pre
        else:  # 删除中间任意节点
            pre = self.__find_pre__(cur)
            pre.next = cur.next

        return self

    # 移除指定值
    def removeItem(self, item) -> object:

        if item == self.head:
            self.head = self.head.next
        elif item == self.tail:
            self.tail = self.__find_pre__(item)
        else:
            self.__find_pre__(item).next = self.__getItemObj__(item).next

        return self

    # 倒序
    def reverseLink(self) -> object:

        pre = None
        head = self.head
        # 假设有3个移动元素，pre\head\next, 每次遍历链表右边移动,并且往左创建指针,直到往右移动的head为none为止,
        # 那么最终head将会变成最尾的元素,每次返回最后一个要往左移的head(即遍历中的pre)
        while head is not None:
            Next = head.next
            head.next = pre
            pre = head
            head = Next

        return pre

    def iternodes(self, reverse=False):

        cur = self.reverseLink() if reverse else self.head
        while cur:
            yield cur
            cur = cur.next

    __iter__ = iternodes

    # 找指定值的前一个节点
    def __find_pre__(self, item) -> object:
        pre = self.head
        item = item if type(item) == ListNode else self.__getItemObj__(item)
        while pre.next != item:
            pre = pre.next

        return pre

    # 获取指定值节点类
    def __getItemObj__(self, item):

        for i in self.iternodes():

            if i.val == item:
                return i
        else:
            raise Exception("can't find")

    def __getitem__(self, offset):
        start = 0 if offset >= 0 else 1
        reverse = False if offset >= 0 else True
        for i, node in enumerate(self.iternodes(reverse), start):
            if i == abs(offset):
                return node
        else:
            raise IndexError


if __name__ == '__main__':
    link1 = SLink()

    link1.append(2)
    link1.append(4)
    link1.append(3)

    link2 = SLink()
    link2.append(5)
    link2.append(6)
    link2.append(4)

    print(link1.iternodes())
    print(link2.iternodes(True))