
__author__ = 'AKV'

'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''


"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random


START_NUM = 100
END_NUM =1000

def _sum(n):
    size = n
    rand_array = [random.randint(START_NUM, END_NUM) for _ in range(size)]

    pos_min, pos_max = 0, 0
    sum_numbers_main = 0

    for i in range(len(rand_array)):
        if rand_array[i] > rand_array[pos_max] :
            pos_max = i
        if rand_array[i] < rand_array[pos_min]:
            pos_min = i

    if pos_min < pos_max:
        for i in range(pos_min + 1, pos_max):
            sum_numbers_main += rand_array[i]
    else:
        for i in range(pos_max + 1, pos_min):
            sum_numbers_main += rand_array[i]

    return sum_numbers_main


'''
100 loops, best of 5: 99.5 usec per loop    -   10
100 loops, best of 5: 800 usec per loop     -   100
100 loops, best of 5: 4.08 msec per loop    -   500
100 loops, best of 5: 8.27 msec per loop    -   1000
'''


def _sum_min_max(n):
    size = n
    rand_array = [random.randint(START_NUM, END_NUM) for i in range(size)]

    _min = min(rand_array)
    _max = max(rand_array)

    index_min = rand_array.index(_min)
    index_max = rand_array.index(_max)

    if index_min < index_max:
        index_min, index_max = index_max, index_min

    sum_num = 0
    for i in range(index_min + 1, index_max):
        sum_num += rand_array[i]

    return sum_num


'''
100 loops, best of 5: 84.3 usec per loop    -   10
100 loops, best of 5: 765 usec per loop     -   100
100 loops, best of 5: 3.75 msec per loop    -   500
100 loops, best of 5: 7.6 msec per loop     -   1000
'''



def insertion(n):
    size = n
    rand_data = [random.randint(START_NUM, END_NUM) for _ in range(size)]

    for i in range(len(rand_data)):
        j = i - 1
        key = rand_data[i]
        while rand_data[j] > key and j >= 0:
            rand_data[j + 1] = rand_data[j]
            j -= 1
        rand_data[j + 1] = key

    return rand_data

'''
100 loops, best of 5: 109 usec per loop     -   10
100 loops, best of 5: 852 usec per loop     -   50
100 loops, best of 5: 3.04 msec per loop    -   100
100 loops, best of 5: 63.9 msec per loop    -   500
'''

'''
Выводы:
1. Первые два алгоритма, хотя и различаются по времени работы алгоритмов,
имеют одинаковую линейную сложность алгоритма O(n). Так как в работе идет только последовательный перебор элементов,
т.е. сложность линейно зависит от величины обрабатываемых данных.

2. Разница во времени работы алгоритма объясняется тем, что в певом случае обход списка осуществляется меньшее число 
раз чем во втором алгоритме.

3. В третьем случае приведен алгоритм сортировки вставками. Сложность этого алгоритма уже не линейная, так как в теле
алгоритма есть несколько вложенных циклов перебирающих список. Поэтому сложность можно оценить как O(n**2). 
Что подтверждается полученными данными оценки времени работы алгоритма. 
'''