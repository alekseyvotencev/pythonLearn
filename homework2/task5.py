# Реализуйте алгоритм перемешивания списка.

from random import randint

N = 20
numbers = []
for i in range(N):
    numbers.append(randint(-N, N))
print(numbers)
for i in range(len(numbers)):
    index = randint(0, len(numbers) - 1)
    temp = numbers[i]
    numbers[i] = numbers[index]
    numbers[index] = temp
print(numbers)
