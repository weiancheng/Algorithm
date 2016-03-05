#!/usr/bin/python

# 2016/2/14
# stack


def test_stack():
    stack = Stack(5)
    stack.add(5)
    stack.add(4)
    stack.add(3)
    stack.add(2)
    stack.add(1)
    stack.add(0)
    print stack.is_full()
    stack.print_all()

    print stack.delete()
    print stack.delete()


class Bag(object):
    def __init__(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def is_full(self):
        pass

    def is_empty(self):
        pass


class Stack(Bag):
    def __init__(self, stack_size):
        self.__size = stack_size
        self.__list = []
        self.__rear = -1
        self.__head = -1
        self.__num = 0

    def add(self, data):
        if self.__num == 0:
            self.__list.insert(0, data)
            self.__rear = 0
            self.__head = 0
            self.__num = 1
        else:
            if self.is_full():
                return False
            self.__rear += 1
            self.__list.insert(self.__rear, data)
            self.__num += 1

        return True

    def delete(self):
        if self.is_empty():
            return False

        data = self.__list.pop(self.__rear)
        self.__rear -= 1
        self.__num -= 1
        return data

    def is_empty(self):
        if self.__num == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.__num == self.__size:
            return True
        else:
            return False

    def print_all(self):
        for i in self.__list:
            print str(i)
