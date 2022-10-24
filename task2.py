# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f'x = {x}, y = {y}, z = {z}')
            print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {not(x or y or z) == (not x or not y or not z)}')
            print('')
