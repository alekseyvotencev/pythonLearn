# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
min = round(lst[0] % 1, 2)
max = round(lst[0] % 1, 2)

for i in range(1, len(lst) - 1):
    if round(lst[i] % 1, 2) < min:
        min = round(lst[i] % 1, 2)
    if round(lst[i] % 1, 2) > max:
        max = round(lst[i] % 1, 2)
print(max - min)
