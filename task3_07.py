
__author__ = 'AKV'

"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
"""
import random
# Generate random array
rand_array = [random.randint(0, 100) for i in range(200)]

print(rand_array)
min_1, min_2 = rand_array[0], rand_array[0]

for value in rand_array:
    if value <= min_1:
        if value <= min_2:
            min_2 = value
        else:
            min_1 = value
    if value <= min_2:
        min_2 = value

print(f'{min_1} - {min_2}')

