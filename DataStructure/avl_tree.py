#!/usr/bin/python

import BinaryTree


def print_array(array):
    for i in array:
        print str(i)


def test_avl_tree():
    at = AVLTree()
    for data in range(10):
        at.avl_insert(data)

    r = []
    at.show(r)
    print_array(r)


class AVLTree(BinaryTree.BinaryTree):
    def __init__(self):
        self.root = None
        self.num = 0

    def avl_insert(self, data):
        if self.root:
            self._insert(self.root, data)
            self._avl_travel_tree(self.root)
        else:
            self.root = BinaryTree.Node(data)
            self.root.right_child = None
            self.root.left_child = None
            self.num = 1

    def _avl_travel_tree(self, node):
        if node.left_child:
            self._avl_travel_tree(node.left_child)

        if node.right_child:
            self._avl_travel_tree(node.right_child)

        self._avl_balanced(node)

    def _get_find_parent(self, data):
        if self.root.data is data:
            return None

        parent = None
        now = self.root

        while True:
            if now.data is data:
                break

            parent = now

            if now.data < data:
                now = now.right_child
            else:
                now = now.left_child

        return parent

    def _avl_rotate_ll(self, node):
        parent = self._get_find_parent(node.data)
        temp = node.left_child.right_child
        node.left_child.right_child = node
        if parent:
            if parent.left_child is node:
                parent.left_child = node.left_child
            else:
                parent.right_child = node.left_child
        else:
            self.root = node.left_child
        node.left_child = temp

    def _avl_rotate_rr(self, node):
        parent = self._get_find_parent(node.data)
        if parent:
            if parent.left_child is node:
                parent.left_child = node.right_child
            else:
                parent.right_child = node.right_child
        else:
            self.root = node.right_child

        temp = node.right_child.left_child
        node.right_child.left_child = node
        node.right_child = temp

    def _avl_rotate_lr(self, node):
        parent = self._get_find_parent(node.data)
        second = node.left_child
        third = node.left_child.right_child
        if parent:
            if parent.left_child is node:
                parent.left_child = third
            else:
                parent.right_child = third
        else:
            self.root = third

        second.right_child = third.left_child
        node.left_child = third.right_child
        third.left_child = second
        third.right_child = node

    def _avl_rotate_rl(self, node):
        parent = self._get_find_parent(node.data)
        second = node.right_child
        third = node.right_child.left_child
        if parent:
            if parent.left_child is node:
                parent.left_child = third
            else:
                parent.right_child = third
        else:
            self.root = third

        node.right_child = third.left_child
        second.left_child = third.right_child
        third.left_child = node
        third.right_child = second

    def _avl_balanced(self, node):
        bf = self._avl_get_balanced_factor(node)
        if bf >= 2:
            # left
            bf = self._avl_get_balanced_factor(node.left_child)
            if bf >= 1:
                self._avl_rotate_ll(node)
            else:
                self._avl_rotate_lr(node)
        elif bf <= -2:
            # right
            bf = self._avl_get_balanced_factor(node.right_child)
            if bf >= 1:
                self._avl_rotate_rl(node)
            else:
                self._avl_rotate_rr(node)

    def _avl_get_balanced_factor(self, node):
        left_height = 0
        right_height = 0

        if node.left_child:
            left_height = self._avl_get_height(node.left_child)

        if node.right_child:
            right_height = self._avl_get_height(node.right_child)

        return left_height - right_height

    def _avl_get_height(self, node):
        left_height = 0
        right_height = 0

        if node.left_child:
            left_height = self._avl_get_height(node.left_child)

        if node.right_child:
            right_height = self._avl_get_height(node.right_child)

        if not node.left_child and not node.right_child:
            return 1

        return left_height + 1 if left_height > right_height else right_height + 1

    def avl_get_node_num(self):
        return self.get_number()

    def avl_remove(self, data):
        self.remove(data)
