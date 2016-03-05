#!/usr/bin/python

# 2016/2/17
# vector

# vector is a data structure which is like a dynamic array,
# user wouldn't assign a size to the vector when it's in initialize.


class Node:
    def __init__(self, value):
        self.data = value
        self.index = -1
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class Vector:
    def __init__(self):
        self.root = None
        self.__num = 0

    def add(self, value):
        if self.__num == 0:
            node = Node(value)
            node.index = 0
            node.next = None
            node.prev = None
            self.root = node
            self.__num = 1
            return

        index = self.get_free_index()
        if index == 0:
            node = Node(value)
            node.index = 0
            node.next = self.root
            node.prev = None
            self.root = node
            self.__num += 1
        else:
            self.insert(index, value)

    def __find_node(self, index):
        node = self.root
        while node:
            if node.index == index:
                break
            node = node.next
        return node

    def get_free_index(self):
        node = self.root
        index_candidate = 0
        while True:
            if not node:
                break
            index = node.index
            if index_candidate < index:
                break
            index_candidate = index + 1
            node = node.next

        return index_candidate

    def get(self, index):
        node = self.__find_node(index)
        return node

    def insert(self, index, value):
        node = self.__find_node(index)
        if node:
            node.data = value
            return

        node = Node(value)
        node.index = index
        pre_node_candidate = None
        now_node = self.root
        while True:
            if not now_node:
                break
            if now_node.index >= node.index:
                break
            pre_node_candidate = now_node
            now_node = now_node.next

        node.next = pre_node_candidate.next
        node.prev = pre_node_candidate
        if pre_node_candidate.next:
            pre_node_candidate.next.prev = node
        pre_node_candidate.next = node
        self.__num += 1

    def remove(self, index):
        node = self.__find_node(index)
        if not node:
            return

        if not node.prev:
            self.root = node.next
            node.next.prev = None
        elif not node.next:
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = None
        del node

    def print_all(self):
        node = self.root
        while node:
            print node
            node = node.next


def main():
    v = Vector()
    v.add(1)
    v.add(2)
    v.add(3)
    v.insert(3, 10)
    print ""
    print v.get(3)
    print ""
    v.print_all()
    v.insert(10, 100)
    print ""
    v.print_all()
    v.insert(6, 99)
    print ""
    v.print_all()
    print ""

    v.remove(2)
    v.remove(0)
    v.print_all()


if __name__ == '__main__':
    main()
