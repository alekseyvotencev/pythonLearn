# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = 2
numbers = [(1 + 1 / i) ** i for i in range(1, n+1)]
sum = 0
for item in numbers:
    sum += item
print(sum)
