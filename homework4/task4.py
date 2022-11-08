# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint


k = int(input('введите k: '))
lst = [randint(0, 101) for i in range(k+1)]
print(lst)
equation = ''
lenght = len(lst)
if lenght < 1:
    equation = 'x = 0'
else:
    for i in range(lenght):
        if i != lenght - 1 and i != lenght-2 and lst[i] != 0:
            equation += f'{lst[i]}x^{lenght - 1 - i}'
            if lst[i+1] != 0:
                equation += ' + '
        elif i == lenght - 2 and lst[i] != 0:
            equation += f'{lst[i]}x'
            if lst[i+1] != 0:
                equation += ' + '
        elif i == lenght - 1 and lst[i] != 0:
            equation += f'{lst[i]} = 0'
        elif i == lenght - 1 and lst[i] == 0:
            equation += ' = 0'
file = open("equation.txt", "w")
file.write(equation)
file.close()
