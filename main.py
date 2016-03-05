#!/usr/bin/python

from DataStructure import BinaryTree
from DataStructure import HashTable
from Algorithm import BinarySearch
from Algorithm import DepthFirstSearch
from DataStructure import Vector
from Algorithm import QuickSort
from DataStructure import avl_tree
from Algorithm import tower_of_hanoi

def test_quick_sort():
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    QuickSort.quick_sort(a, 0, len(a)-1)
    for i in a:
        print str(i)


def test_hash_table():
    hash_table = HashTable.HashTable(100)
    print "hash key(10): " + str(hash_table.hash_table_put(10))
    print "hash key(100):" + str(hash_table.hash_table_put(100))
    print "hash key(1000):" + str(hash_table.hash_table_put(1000))
    print "hash key(10000):" + str(hash_table.hash_table_put(10000))
    print hash_table.hash_table_is_in_table(199)
    print hash_table.hash_table_get_by_key(0)
    print hash_table.hash_table_get_by_key(0)


def test_binary_search():
    l = [2, 4, 6, 8, 10]
    bs = BinarySearch.binary_search(l, 2)
    print str(bs)


def test_depth_first_search():
    stack = DepthFirstSearch.Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.show()


def test_vector():
    v = Vector.Vector()
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


def test_binary_tree():
    bt = BinaryTree.BinaryTree()
    data = [50, 20, 90, 10, 30, 70, 100, 5, 15, 25, 40, 60, 80, 95, 101]
    for d in data:
        bt.insert(int(d))

    array = []
    bt.show(array)
    for i in array:
        print str(i)

    bt.remove(20)

    array2 = []
    bt.show(array2)
    for i in array2:
        print str(i)


def main():
    # test_binary_tree()
    # Recursion.test_fibonacci()
    # test_quick_sort()
    # test_hash_table()
    # test_binary_search()
    # test_depth_first_search()
    #avl_tree.test_avl_tree()
    tower_of_hanoi.test_hanoi(3)


if __name__ == '__main__':
    main()