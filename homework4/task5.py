# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
file1 = open('eq1.txt', 'r')
file2 = open('eq2.txt', 'r')

for line in file1:
    list1 = line.split()
print(list1)
degrees1 = {}
for i in range(len(list1)-1):
    # print(list1[i])
    if (list1[i] != '+' and list1[i] != '-'):
        if len(list1) > 1:
            degrees1[list1[i].split('x')[0]] = list1[i].split('x')[1]
        l = list1[i].split('x')
        print(l)

file1.close()
file2.close()
