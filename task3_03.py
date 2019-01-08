
__author__ = 'AKV'

"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

rand_array = [random.randint(0, 100) for i in range(100)]

position_min = 0
position_max = 0

for i in range(100):
    if rand_array[i] > rand_array[position_max]:
        position_max = i
    if rand_array[i] < rand_array[position_min]:
        position_min = i

rand_array[position_min], rand_array[position_max] = rand_array[position_max], rand_array[position_min]

print(f"Минимальные и максимальные элементы под номером {position_min} и {position_max} поменяны местами.")

