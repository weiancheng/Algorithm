#!/usr/bin/python

# 2016/2/14

# queue


def test_queue():
    queue = Queue(5)
    queue.add(1)
    print "is empty: " + str(queue.is_empty())
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.add(6)
    print "is full: " + str(queue.is_full())
    queue.print_all()
    print "====================="
    print queue.delete()
    print queue.delete()
    print "======================"
    queue.add(6)
    queue.add(7)
    queue.add(8)
    queue.print_all()
    print "====================="
    print queue.delete()
    print "====================="
    queue.add(9)
    queue.print_all()


class Queue(object):
    def __init__(self, queue_size):
        self.__list = []
        for i in range(queue_size):
            self.__list.append(None)
        self.__size = queue_size
        self.__head = -1
        self.__rear = -1
        self.__num = 0

    def add(self, data):
        if self.is_empty():
            self.__head = 0
            self.__rear = 0
            self.__num = 1
            self.__list[0] = data
        else:
            if self.is_full():
                return False

            self.__rear += 1
            if self.__rear == self.__size:
                self.__rear = 0
            self.__list[self.__rear] = data
            self.__num += 1

        return True

    def delete(self):
        if self.is_empty():
            return False

        data = self.__list[self.__head]
        self.__list[self.__head] = None
        self.__head += 1
        if self.__head > self.__size:
            self.__head = 0
        self.__num -= 1
        return data

    def is_full(self):
        if self.__num == self.__size:
            return True
        else:
            return False

    def is_empty(self):
        if self.__num == 0:
            return True
        else:
            return False

    def print_all(self):
        for i in self.__list:
            print str(i)
