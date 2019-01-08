
__author__ = 'AKV'

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
count = 0

# 1 решение1


for i in range(START_NUM, END_NUM + 1):
    result = True
    for x in range(START_DIV, END_DIV + 1):
        if i % x == 0:
            result = False
            break

    if not result:
        count += 1


print(f"В диапазоне от {START_NUM} до {END_NUM} нашлось {count} чисел кратных любому числу от {START_DIV} до {END_DIV}")
