#!/usr/bin/python

# 2016/2/17
# the algorithm in hash table is: value % the size of the hash table,
# if the content of the key in hash table is not blank, then add one to key value,
# meant program would find the next content of the key in hash table.
# the key point of hash table is the algorithm that how to get the key by value.

class HashTable:
    def __init__(self, hash_table_size=100):
        self.__hash_table_size = hash_table_size
        self.table = []
        for i in range(hash_table_size):
            self.table.insert(i, '*')

    def hash_table_put(self, value):
        key = self.__generate_key(value)
        self.table.insert(key, value)
        return key

    def __generate_key(self, value):
        key = -1
        start_key = value % self.__hash_table_size
        for i in range(start_key, self.__hash_table_size):
            if self.table[i] == '*':
                key = i
                break

        if key == -1:
            for i in range(0, start_key):
                if self.table[i] == '*':
                    key = i
                    break
        return key

    def __find_key(self, value):
        key = -1
        start_key = value % self.__hash_table_size
        for i in range(start_key, self.__hash_table_size):
            if self.table[i] == value:
                key = i
                break

        if key == -1:
            for i in range(start_key):
                if self.table[i] == value:
                    key = i
                    break

        return key

    def hash_table_get_by_key(self, key):
        value = self.table[key]
        if value == '*':
            return None
        else:
            return value

    def hash_table_get_by_value(self, value):
        key = self.__find_key(value)
        if key == -1:
            return None
        return key

    def hash_table_del_by_value(self, value):
        key = self.__find_key(value)
        if key != -1:
            self.table[key] = '*'
            return True
        else:
            return False

    def hash_table_del_by_key(self, key):
        if key >= self.__hash_table_size:
            return False

        self.table[key] = '*'
        return True

    def hash_table_is_in_table(self, value):
        key = value % self.__hash_table_size
        if self.table[key] == value:
            return True
        else:
            for i in range(self.__hash_table_size):
                if self.table[i] == value:
                    return True

            return False
