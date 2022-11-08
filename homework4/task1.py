# Вычислить число c заданной точностью d

from math import pi

d = float(input('введите d: '))
count = 0
while d != 1:
    d *= 10
    count += 1
print(count)
print(f'число Пи с точность d = {d} π = {round(pi, count)}')
