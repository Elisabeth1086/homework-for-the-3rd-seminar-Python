# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число, которое хотите найти в массиве: '))

import random
a = []
count = 0
for i in range(n):
        a.append(random.randint(1, n+1))
        if a[i] == x:
            count += 1
print(f'Число {x} встречается {count} раз')

print(a)