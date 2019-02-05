
__author__ = 'AKV'

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами 
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована 
в виде функции. По возможности доработайте алгоритм (сделайте его умнее)
"""

import random

MIN = -100
MAX = 99


def get_random_array(n):
    _array = [random.randint(MIN, MAX) for _ in range(n)]
    return _array


def sort_bubbles(_array):
    n = 1

    while n < len(_array):
        for i in range(len(_array) - n):
            if _array[i] < _array[i + 1]:
                _array[i], _array[i + 1] = _array[i + 1], _array[i]

        n += 1


array = get_random_array(20)
print(array)
sort_bubbles(array)
print(array)

