# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
from random import randint
n = int(input('Введите количество чисел: '))
list = [randint(1, 10) for i in range(n)]
print(list)
def SumOfNumbers(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum = sum + list[i]
    return sum

print(SumOfNumbers(list))