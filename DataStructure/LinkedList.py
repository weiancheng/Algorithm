#!/usr/bin/python

class Node(object):
    def __init__(self, data):
        self.Data = data
        self.Prev = None
        self.Rear = None

    def __str__(self):
        return str(self.Data)

class MyList(object):
    def __init__(self):
        self.__mList = []
        self.__mHead = None
        self.__mTail = None
        self.__mLength = 0

    def addNode(self, data):
        # create a new node
        node = Node(data)

        # find a fit place, loop this list, and check data
        if self.__mLength == 0:
            self.__mHead = node
            self.__mTail = node
            node.Prev = node
            node.Rear = node
        else:
            now = self.__mHead
            while now != None:
                if now.Data <= node.Data:
                    if now == self.__mTail:
                        now = None
                    else:
                        now = now.Rear
                        continue
                break

            if now == None:
                node.Prev = self.__mTail
                node.Rear = self.__mHead
                self.__mTail.Rear = node
                self.__mTail = node
            else:
                now.Prev.Rear = node
                node.Prev = now.Prev
                node.Rear = now
                now.Prev = node

            if now == self.__mHead:
                self.__mHead = node

        # add length
        self.__mLength += 1

        # push into list
        self.__mList.append(node)

    def getLength(self):
        return self.__mLength

    def delNode(self, data):
        node = self.searchNode(data)
        if not node:
            return

        if self.__mHead == node:
            self.__mHead = node.Rear

        if self.__mTail == node:
            self.__mTail = node.Prev

        prev = node.Prev
        rear = node.Rear
        prev.Rear = rear
        rear.Prev = prev
        node.Prev = None
        node.Rear = None
        self.__mList.remove(node)
        self.__mLength -= 1
        del node

    def searchNode(self, data):
        node = self.__mHead
        while node:
            if node.Data == data:
                break
            if node == self.__mTail:
                node = None
                break
            node = node.Rear
        return node

    def isNode(self, data):
        node = self.searchNode(data)
        if node:
            return True
        else:
            return False

    def print_data(self):
        now = self.__mHead
        while True:
            print now
            if self.__mTail == now:
                break
            else:
                now = now.Rear


def main():
    my_list = MyList()
    my_list.addNode(100)
    my_list.addNode(10)
    my_list.addNode(50)
    my_list.addNode(20)
    my_list.addNode(5)
    my_list.print_data()
    print my_list.getLength()
    print "**********************"
    my_list.delNode(20)
    my_list.print_data()
    print my_list.getLength()

if __name__ == '__main__':
    main()