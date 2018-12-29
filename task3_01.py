
__author__ = 'AKV'

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
count = 0

def rate(number):
    result = False
    for x in range(START_DIV, END_DIV + 1):
        if x

# 1 решение1
for i in range(START_NUM, END_NUM + 1):
    result = False
    for x in range(START_DIV, END_DIV + 1):
        if i % x == 0:
            break
        else:
            if x == END_DIV:
                count += 1


print(f"В диапазоне от {START_NUM} до {END_NUM} нашлось {count} чисел.")

'''
# 2 решение
num_list = [num for num in range(START_NUM, END_NUM+1)]
for
'''