#!/usr/bin/python

#
# 2016/2/19
# Bread First Search
#


import Queue
import BinaryTree


class BreadFirstSearch:
    def __init__(self):
        self.bt = BinaryTree.BinaryTree()

    def insert(self, data):
        self.bt.insert(data)

    def bfs(self, array):
        queue = Queue.Queue()
        queue.put(self.bt.root)

        while True:
            if queue.empty():
                break

            n = queue.get()

            array.append(n)

            if n.left_child:
                queue.put(n.left_child)

            if n.right_child:
                queue.put(n.right_child)