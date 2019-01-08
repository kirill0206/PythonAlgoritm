
__author__ = 'AKV'

"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random
# Generate random array
rand_array = [random.randint(0, 100) for i in range(100)]

#get dict, keys - number in random array, value - count keys in array
result = {}
for i in range(len(rand_array)):
    if result.get(rand_array[i]) is None:
        result[rand_array[i]] = 1
    else:
        result[rand_array[i]] += 1

#get maximum from dict
maximum = 1
for value in result.values():
    if value > maximum:
        maximum = value

for key, value in result.items():
    if value == maximum:
        print(f"Число {key} встретилось в массиве максимальное число раз - {value}")
        break
