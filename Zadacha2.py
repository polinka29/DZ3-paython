# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint
num = []
for i in range(randint(3, 5)):
    num.append(randint(2, 7))
res = []
for i in range((len(num) // 2)):
    res.append(num[i] * num[len(num) - 1 - i])
print(num, res, sep=' - ')