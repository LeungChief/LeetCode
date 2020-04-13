class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __repr__(self):
        return '{}'.format(self.item)


# 双向链表
class DLink:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.__size += 1
        return self

    def pop(self):
        if self.head is None:
            raise Exception('Empty')
        else:
            node = self.tail
            item = node.item
            prev = node.prev
            if prev is None:
                self.head = None
                self.tail = None
            else:
                self.tail = prev
                prev.next = None
            self.__size -= 1
            return item

    def iternodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def insert(self, index, item):
        if index < 0:
            raise IndexError

        for i, nodes in enumerate(self.iternodes()):
            if i == index:
                current = nodes
                break
        else:
            self.append(item)
            return

        node = Node(item)
        prev = current.prev
        next = current
        if prev is None:
            self.head = node
            node.next = next
            next.prev = node
        else:
            next.prev = node
            prev.next = node
            node.prev = prev
            node.next = next
        self.__size += 1

    def remove(self, index):

        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise IndexError

        for i, nodes in enumerate(self.iternodes()):
            if i == index:
                current = nodes
                break
        else:
            raise IndexError

        prev = current.prev
        next = current.next
        # 有四种情况
        if prev is None and next is None:
            self.head = None
            self.tail = None
        elif prev is None:
            self.head = next
            next.prev = None
        elif next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev
        del current
        self.__size -= 1

    __iter__ = iternodes

    def __getitem__(self, index):
        start = 0 if index >= 0 else 1
        reverse = False if index >= 0 else True
        for i, node in enumerate(self.iternodes(reverse), start):
            if i == abs(index):
                return node
        else:
            raise IndexError

    def __setitem__(self, index, value):
        self[index].item = value


if __name__ == '__main__':
    l = DLink()
    l.append([123, 3444])
    l.append([3])
    l[0] = 3
    print(list(l.iternodes()))
