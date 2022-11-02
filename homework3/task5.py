# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def negafib(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return negafib(n-2) - negafib(n-1)


lst = [0]
k = 8
for i in range(1, k + 1):
    lst.append(fib(i))
    lst.insert(0, negafib(i))
print(lst)
