# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

N = 20
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)
file = open('file.txt', 'r')
multiplication = 1
for line in file:
    if int(line) < len(numbers) - 1:
        multiplication *= numbers[int(line)]
file.close()
print(multiplication)
