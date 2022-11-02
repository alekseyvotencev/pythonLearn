# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = 45
result = ''

while number != 0:
    result = str(number % 2) + result
    number = number // 2
print(result)
