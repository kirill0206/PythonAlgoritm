
__author__ = 'AKV'

"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections


class MyNode():
    def __init__(self, number, value, left=None, right=None):
        self.number = number
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'number = {self.number}\tvalue = {self.value}'


def search(tree, number, path = ''):
    if tree.number == number:
        return path
    if number < tree.number and tree.left is not None:
        path = f'{path}0'
        search(tree.left, number, path)
    if number > tree.number and tree.left is not None:
        path = f'{path}1'
        search(tree.right, number, path)
    else:
        print('Ошибка поиска')
        exit(0)


_str = dict(collections.Counter('abrakadabro'))
print(_str)
keys = list(_str.keys())
keys = keys[::-1]
print(keys)

_list = []
code = {}

for key in keys:
    _list.append(MyNode(_str[key], key))

while len(_list) > 1:
    left = _list.pop(0)
    right = _list.pop(0)

    number = left.number + right.number
    node = MyNode(number, number, left, right)

    if len(_list) == 0:
        _list.append(node)
        break

    if number < _list[0].number:
        _list.insert(0, node)

    i = 0
    while i < len(_list) - 1:
        if _list[i].number <= number < _list[i+1].number:
            _list.insert(i+1, node)
            break
        i += 1
    else:
        _list.append(node)

print(_list)

for key in keys:
    code.update({key: search(_list[0], _str[key])})

print(code)


