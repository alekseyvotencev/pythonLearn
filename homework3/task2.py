# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

lst = [2, 3, 4, 5, 6]
result_lst = []

middle = len(lst)
for i in range(math.ceil(middle/2)): # почитал про round - оказывается недавно обновили, и он теперь 2.5 округляет до 2
    result_lst.append(lst[i] * lst[middle - 1 - i])
print(result_lst)
