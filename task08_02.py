
__author__ = 'AKV'

"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
import collections


class MyNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def search(tree, number, path = ''):
    if tree.value == number:
        return path
    if number < tree.value and tree.left is not None:
        search(tree.left, number)
    if number > tree.value and tree.left is not None:
        search(tree.right, number, path)
    else:
        print('Ошибка поиска')
        exit(0)


def get_tree(_dict):


#_str = collections.Counter(input("Введите строку:"))

_str = dict(collections.Counter('abrakadabro'))
print(_str)

