#!/usr/bin/python

from DataStructure import BinaryTree


def show_list(l):
    print "node num: " + str(len(l))
    for i in l:
        print str(i)

    print "*** end ***"


def test_dfs():
    bt = BinaryTree.BinaryTree()
    bt.insert(12)
    bt.insert(13)
    bt.insert(14)
    bt.insert(1)
    bt.insert(3)
    bt.insert(2)
    bt.insert(4)
    bt.insert(5)

    array = []
    print "in-ordered"
    dfs_inordered(bt.root, array)
    show_list(array)
    print ""
    print "pre-ordered"
    array2 = []
    dfs_preordered(bt, array2)
    show_list(array2)
    print ""
    print "post-ordered"
    array3 = []
    dfs_postordered(bt, array3)
    show_list(array3)


def dfs_postordered(node, array):
    if node.left_child:
        dfs_postordered(node.left_child, array)

    if node.right_child:
        dfs_postordered(node.right_child, array)

    array.append(node.data)


def dfs_preordered(node, array):
    if node.left_child:
        dfs_preordered(node.left_child, array)

    array.append(node.data)

    if node.right_child:
        dfs_preordered(node.right_child, array)


def dfs_inordered(node, array):
    array.append(node.data)

    if node.left_child:
        dfs_inordered(node.left_child, array)

    if node.right_child:
        dfs_inordered(node.right_child, array)

