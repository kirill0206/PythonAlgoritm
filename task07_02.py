
__author__ = 'AKV'

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами 
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

MIN = 0
MAX = 50


def get_random_array(n):
    _array = [random.random()*(MAX - MIN) + MIN for _ in range(n)]
    return _array


def merge_array(array_a, array_b):
    result = []
    i = 0
    j = 0
    while i < len(array_a) and j < len(array_b):
        if array_a[i] <= array_b[j]:
            result.append(array_a[i])
            i += 1
        else:
            result.append(array_b[j])
            j += 1
    result += array_a[i:] + array_b[j:]
    return result


def merge_sort(_array):
    if len(_array) <= 1:
        return _array
    _array_left = _array[:(len(_array) // 2)]
    _array_right = _array[(len(_array) // 2):]
    return merge_array(merge_sort(_array_left), merge_sort(_array_right))


array = get_random_array(9)
print(array)
print(merge_sort(array))
