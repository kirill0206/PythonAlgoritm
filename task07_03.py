
__author__ = 'AKV'

"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше 
медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""

import random

MIN = 0
MAX = 100


def get_random_array(n):
    n = 2 * n + 1
    _array = [random.randint(MIN, MAX) for _ in range(n)]
    return _array


def get_mediana(_array):
    for i in range(len(_array)):
        count_more = 0
        count_less = 0
        for j in range(len(_array)):
            if _array[i] != _array[j]:
                if _array[i] > _array[j]:
                    count_more += 1
                else:
                    count_less += 1

        if count_less == count_more:
            return _array[i]


array = get_random_array(5)
print(array)
print(get_mediana(array))
