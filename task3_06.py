
__author__ = 'AKV'

"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random
# Generate random array
rand_array = [random.randint(0, 100) for i in range(100)]

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

print(f"Сумма элементов между максимальным и минимальным равно {sum_numbers_main}")
