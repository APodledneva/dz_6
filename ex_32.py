# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

size = int(input())
my_list = [random.randint(-10, 10) for _ in range(size)]
print(my_list)
my_list2 = []

min_dip = int(input('Введите минимальное число диапазона '))
max_dip = int(input('Введите максимальное число диапазона '))

for i in range(len(my_list)):
    if min_dip < my_list[i] < max_dip:
        my_list2.append(i)

print(my_list2)