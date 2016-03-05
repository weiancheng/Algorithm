#!/usr/bin/python

#
# 2016/2/19
# Binary Tree
# focus on how to build a binary tree:
#   insert a new node.
#   search the while tree.
#
# reference: http://www.cprogramming.com/tutorial/lesson18.html
#


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, data):
        if self.root:
            self._insert(self.root, data)
        else:
            self.root = Node(data)
            self.root.right_child = None
            self.root.left_child = None
            self.num = 1

    def _insert(self, node, data):
        if data >= node.data:
            # right child
            if not node.right_child:
                new_node = Node(data)
                new_node.right_child = None
                new_node.left_child = None
                node.right_child = new_node
                self.num += 1
            else:
                self._insert(node.right_child, data)
        elif data < node.data:
            # left child
            if not node.left_child:
                new_node = Node(data)
                new_node.right_child = None
                new_node.left_child = None
                node.left_child = new_node
                self.num += 1
            else:
                self._insert(node.left_child, data)

    def get_number(self):
        return self.num

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node:
            if data >= node.data:
                return self._search(node.right_child, data)
            elif data < node.data:
                return self._search(node.left_child, data)
            elif data == node.data:
                return node
        else:
            return None

    def show(self, array):
        self._show(self.root, array)

    # post-ordered search
    def _show(self, node, array):
        if node.left_child:
            self._show(node.left_child, array)

        if node.right_child:
            self._show(node.right_child, array)

        array.append(node.data)
        return

    def remove(self, data):
        if not self.root:
            # an empty tree
            return

        parent = None
        node = self.root

        while True:
            if node:
                if data > node.data:
                    parent = node
                    node = node.right_child
                elif data < node.data:
                    parent = node
                    node = node.left_child
                elif data == node.data:
                    break
            else:
                break

        if not node:
            # not exist
            return

        # remove leaf
        if not node.right_child and not node.left_child:
            if node == self.root:
                self.root = None
            else:
                if parent.right_child == node:
                    parent.right_child = None
                else:
                    parent.left_child = None

            del node
            return

        # single child
        if not node.right_child and node.left_child or not node.left_child and node.right_child:
            # left is single child
            if not node.right_child and node.left_child:
                if self.root == node:
                    self.root = node.left_child
                else:
                    if parent.right_child == node:
                        parent.right_child = node.left_child
                    else:
                        parent.left_.child = node.left_child

                node.left_child = None
                del node

            # right is single child
            elif not node.left_child and node.right_child:
                if self.root == node:
                    self.root = node.right_child
                else:
                    if parent.right_child == node:
                        parent.right_child = node.right_child
                    else:
                        parent.left_child = node.right_child

                node.right_child = None
                del node

            return

        # two child
        if node.right_child and node.left_child:
            smallest_parent = None
            smallest = None
            current = node.right_child
            while True:
                if current.left_child:
                    smallest_parent = current
                    current = current.left_child
                else:
                    smallest = current
                    break

            if smallest:
                smallest.left_child = node.left_child
                smallest.right_child = node.right_child
                smallest_parent.left_child = None

                if node == self.root:
                    self.root = smallest
                else:
                    if parent.right_child == node:
                        parent.right_child = smallest
                    else:
                        parent.left_child = smallest

                del node
        return
