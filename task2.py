# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


a = int(input('введите число: '))
result_list = [factorial(i) for i in range(1, a + 1)]
print(result_list)