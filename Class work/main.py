#                                             Занятие № 1

# name_new = "Rishat"  # строчный комментарий
# age = 35
# print('Hello ' + name_new + '. I am ' + str(age))
# name = 3
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, 'Hello', 9.2
# print(a, b, c)

# import keyword
# print(keyword.kwlist)

# a = 5
# print(a)
# a = 6
# print(a)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print('a:', a)
# print('b:', b)
# c = a  # c = 1
# a = b  # a = 2
# b = c  # b = 1

# a, b = b, a
# print('a:', a)
# print('b:', b)

# # print("строка \n Текстовые последовательности \
# символов")
# print('строка \
# символов')

# print("Документ \"script.py\" находится \r \
# по заданному пути: \n\t D:\\Pyton\\project")

# print(type(-58767868))
# print(type(4.87989))
# print(4456546546546546565489896)
# print(4.4456546546546546565489896)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 ** 2)
# print(5 % 2)

# a = 5
# b = 7
# c = 3
# s = a + b + c
# print('Сумма:', a)
# print('Произведение:', a * b * c)
# print('Среднее арифметическое:', s / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)

# num = 4321
# print('Исходное число:', num)
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a*1000 + b*100 + c*10 + d)

# num = 9753
# print('Исходное число:', num)
# res = (num % 10) * 1000
# num = num // 10  # 432
# res += (num % 10) * 100
# num = num // 10  # 43
# res += (num % 10) * 10
# num = num // 10  # 4
# res += num % 10
# print(res)

# a = int(input('Введите число:'))
# print(a * 2)

#                                             Занятие № 2

# a = 10
# b = 2
# print('a:', a)
# print('b:', b)
# a = a + b  # a = 10 + 2 = 12
# b = a - b  # b = 12 - 2 = 10
# a = a - b  # a = 12 - 10 = 2
# print('a:', a)
# print('b:', b)

# Функции преобразования типов
# int() - числовой тип
# str() - строковый тип
# float() - вещественный тип
# bool() - булевый тип

# num1 = '2'
# num2 = 3
# res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.8))
# print(round(3.894, 2))

# print(5 / 2)

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)
# print(type(c))

# name = 'Виктор'
# age = 28
# print('Меня зовут', name + '. Мне', age, 'лет.')
# print('Меня зовут ', name + '. Мне ', age, ' лет.', sep='---', end='\n\n')
# print('Я учу Python')

# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# res = num ** power
# print('Число', num, 'в степень', power, 'равно:', res)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# print(bool('python'))
# print(bool(' '))
# print(bool(''))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(type(test))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 5)
# print(8 <= 5)
# print('привет' > 'Привет')

# print(2 < 14 < 9)
# print(2 * 5 > 7 >= 4 + 3)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else:
#     print('Доступ запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif a < b:
#     print('b > a')
# else:
#     print('b == a')

# if a > b:
#     print('a > b')
# if a < b:
#     print('b > a')
# if a == b:
#     print('b == a')

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))

# if a == b == c:
#     print('Треугольник равноcторонний')
# if a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# if a != b and a != c and b != c:
#     print('Треугольник разносторонний')

# if a == b == c:
#     print('Треугольник равноcторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('Такого дня недели не существует!')

# month = int(input('Введите номер месяца (цифрой): '))
# if 3 <= month <= 5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# elif month == 12 or month == 1 or month == 2:
#     print('Зима')
# else:
#     print('Такого месяца не существует!')

# n = int(input('Введите количество ворон: '))
# if 0 <= n <= 9:
#     if n == 1:
#         print('На ветке', n, 'ворона')
#     if 2 <= n <= 4:
#         print('На ветке', n, 'вороны')
#     # else:
#     if 5 <= n <= 9 or n == 0:
#         print('На ветке', n, 'ворон')
# else:
#     print('Ошибка ввода данных')

# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

#                                             Занятие № 3

# a = input('Введите первое число:')
# b = input('Введите второе число:')
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)

# i = 1000
# while i >= 1:
#         print(i, end=" ")
#         i //= 10

# i = 0
# a = int(input('Укажите количество символов:'))
# while i < a:
#     print('*', end='')
#     i += 1

# n = int(input('Укажите количество символов:'))
# while n > 0:
#     print('*', end='')
#     n -= 1

# i = 0
# n = 0
# a = int(input('Введите начало диапазона:'))
# b = int(input('Введите конец диапазона:'))
# while a <= b:
#     if a % 2:
#         n = n + a
#     a += 1

# i = 0
# while i < 10:
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен!')

# res = 1
# while True:
#     n = int(input('Введите число:'))
#     if n == 0:
#         break
#     res = res * n
# print('Результат:', res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i +=1
# else:
#     print('Цикл окончен, i =', i)

#                                             Занятие № 4

# n = int(input('Введите количество символов: '))
# sim = input('Тип символа: ')
# orient = input('0 - горизонтальная\n1 - вертикальная\nориентация линии: ')
# i = 0
# while i < n:
#     if orient == '0':
#         print(sim, end=" ")
#     elif orient == '1':
#         print(sim)
#     else:
#         print('Такой ориентации не предусмотренно')
#         break
#     i += 1

# n = int(input('Введите количество чисел последовательности: '))
# i = 0
# summa = maxim = minim = a = float(input('Введите число: '))
# while i < n - 1:
#     a = float(input('Введите число: '))
#     if a < minim:
#         minim = a
#     if a > maxim:
#         maxim = a
#     summa += a
#     i += 1
# print('Количество чисел:', n)
# print('Среднее арифметическое:', summa / n)
# print('Минимальное число:', minim)
# print('Максимальное число:', maxim)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 15:
#         if i % 2 == 0:
#             print('+', end = '')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#   print(element)

# for i in 5, 6, 7, 8, 9:
#     print(i)

# for i in 'Hello':
#     print(i)

# range(start, stop, step)
# print(range(4, 6))

# for i in range(1, 6, 1):
#     print(i)

# for i in range(6, 1, -1):
#     print(i)

# for i in range(100, 0, -10):
#     print(i, end=' ')

# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i, end=' ')
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('----')

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника: "))
# for i in range(h):
#     for j in range(12):
#         print('*', end='')
#     print()

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника: "))
# for i in range(h):
#     for j in range(12):
#         print('*', end='')
#     print()

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(" ", end='')
#     print()

# n = [i for i in range(6)]
# print(n)

# n = [i * 2 for i in "Hello"]
# print(n)

# n = [i for i in range(6) if i % 2 == 0]
# print(n)

# Список class 'list'
# n = [5, 6, 7, 8, 9, 'Hello', 5.6, True]
# print(n)
# print(type(n))

# n = [5, 6, [7, 8, 9], 'Hello', 5.6, True]
# print(n)
# print(type(n))
# print(n[0])
# print(n[2])
# print(n[2][2])
# print(n[3][1])
#
# print(n[-1])
# print(n[-2])

# n = [5, 6, [7, 8, 9], 'Hello', 5.6, True]
# n[1] = 256
# n[0] += 100
# n[3] += '100'
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print(s)

# b = list('Hello')
# print(b)

# s = [1, 2, 3]
# print(s * 2)
# print([5] * 6)

#                                             Занятие № 5

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n == n2:
#     print('Списки равны')
# else:
#     print('Списки разные')
# if n is n2:
#     print('Списки равны')
# else:
#     print('Списки разные')

# [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# for i in range(1, n + 1):
#     print(i ** 2, end=' ')

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = input('->')
# print(a)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)

# print([int(input('-> ')) for i in range(int(input('n = ')))])

# n = [2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=' ')
# print()
# for elem in n:
#     print(elem, end=' ')

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# b = 0
# for i in a:
#     if i < 0:
#         b += i
# print('Сумма отрицательных элементов:', b)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print('Сумма отрицательных элементов:', b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print('Количество четных элементов: ', k)
# print('Сумма нечетных элементов: ', s)

# n = [int(input('-> ')) for i in range(int(input('n = ')))]
# s = 0
# k = 0
# for i in n:
#     if i != 0:
#         s += i
#         k += 1
# print('Среднее арифметическое:', s / k)

#                                             Занятие № 6

# a = [7, 9, 2, 1, 17]
# a[0], a[4] = a[4], a[0]
# a[0], a[-1] = a[-1], a[0]  # более правильно если первый и последний элемент
# print(a)

# Срез
# список[start:stop:step]

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])  # выведет все
# print(s[1:4])  # с первого до четвертого
# print(s[2:])  # со второго до конца
# print(s[:2])  # от начала до второго
# print(s[::2])  # каждый второй элемент
# print(s[::-1])  # разварачивает список
# print(s[1:5:1])
# print(s[5:1:-1])
# print(s[-1::])
# print(s[-3:1:-1])
# print(s[4:1:-1])
# print(s[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[1:3] = [20]
# print(s)
# s[2] = 30
# s[-1:] = [9, 8, 8, 8, 8]
# print(s)
# s[10:] = [9, 18, 28, 38, 48]
# print(s)
# print(s[10])

# Методы списков

# s.append(99)  # добавляет один элемент в конец списка
# s.extend([1, 2, 3])  # добавляет список в конец основного списка
# s.extend('add')
# s.insert(1,100)  # добавляет элемент по индексу (1 параметр), с заданым значением (2 параметр)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     s.append(x)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('-> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 12, 13]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)

# s = [5, 9, 3, 7, 1, 8]
# s[3:] = []
# print(s)
# s.remove(9)  # удаляет первый элемент из списка по значению
# print(s)
# last = s.pop(-2)  # без парамметров - удаляет последний элемент из списка, указанный парамметр - индекс удаляемого
# элемент
# print(last)
# print(s)
# s.clear()  # удаляет из списка все элементы
# print(s)
# del s[2]
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     s.append(x)
# print('Введите индекс:')
# k = int(input('k = '))
# s.pop(k)
# print(s)

# s = [5, 9, 3, 7, 1, 8, 3, 9, 8, 9, 3]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(3, 9)  # передает индекс числа (первый парам), с какого числа искать второй парам.
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print('a =', a)
# print('b =', b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print('a =', a)
# print('b =', b)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# print(s)
# s.reverse()  # перевараивает список
# print(s)
# s.sort(reverse=True)  # сортирует в порядке возрастания, изменяет список
# print(s)
# a = sorted(s, reverse=True)  # сортирует в порядке возрастания, НЕ изменяет исходный список
# print(a)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)  # key=len - сортировка по количеству символов
# print(s2)

#                                             Занятие № 7

# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):  # от 0 до 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # от 3 до 5
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)

# import random

# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))


# from random import randint, randrange
# from random import *

# print(randint(10, 15))
# print(randrange(0, 10, 2))

# import random as r
#
# print(r.randint(10, 15))
# print(r.randrange(0, 10, 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
#
# s = [55, 66, 77, 88, 99, 50, 20, 30, 40, 60, 70, 80, 90]
# print(r.choice(s))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
#
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# import random as r
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# Функция агрегирования

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# sum = [1, 2, 3]
# print(min(sum))
# print(sum(lst))

# import random as r
# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# m = max(x)
# print('Max:', m)
# x.remove(m)
# x.insert(0, m)
# print(x)

# import random as r
# x = [r.randint(-20, 20) for i in range(10)]
# print(x)
# x.sort(reverse=True)
# # x.reverse()
# print(x)

# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# a = min(x)
# print("min:", a)
# b = x.index(a)
# print('index:', b)
# del x[:b]
# print(x)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# if len(lst) == 0:
#     print('Список пуст')

# if not lst:
#     print('Список пуст')

# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print('a =', a)
# print('b =', b)
# c = a + b
# print('c = ', c)

# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for i in b:
#     if i not in c:
#         c.append(i)
# print('Элементы обоих списков без повторений', c)

# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print('Элементы общие для обоих списков:', c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t\t')
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t\t')
#     print()

# a = [1, 2, 3]
# print(a)
# for i in range(len(a)):
#     print(a[i], end='\t')

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# print(a)
# for x, y in a:
#     print(x, '+', y, '=', x + y)

# m = [[r.randint(-10, 20) for x in range(8)] for y in range(4)]
#
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()
#     print(row, end='\t\t')

#                                             Занятие № 8

# import math

# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(math))
# print(math.pi)

# rd = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * math.pi * rd, 2))

# import time

# seconds = time.time()
# print('Секунды с начала эпохи: ', seconds)
# locale_time = time.ctime()
# print('Местное время:', locale_time)
# res = time.localtime()
# print('Localtime:', res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
# print(time.strftime('Today is %B %d, %Y.'))
# print(time.strftime('%d/%m/%Y, %I:%M:%S'))
# print(time.strftime('%d/%m/%Y, %I:%M:%S', time.localtime(4565343442)))


# pause = 5
# print('Program started...')
# time.sleep(pause)
# print(pause, 'seconds.')

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'seconds.')

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, 'second.')

# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
#
# print(time.strftime('Сегодня: %B %d, %Y.'))

# Функция

# print()
#
#
# def hello(name):  # агументы
#     print('Hello', name)
#
#
# hello('Irina')  # параметры
# hello('Igor')


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum('abc', 'def')
# get_sum(2.5, 4.3)


# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end='')
#         else:
#             print(c, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     print(a + b)
#     return a + b
#
#
# res = get_sum(1, 8)
# print(res)
# print(get_sum(2, 5))


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def funk(x, y):
#     if x < y:
#         return x + y
#     else:
#         return x - y
#
#
# a = int(input('a = '))
# b = int(input('b = '))
# print('Результат: ', funk(a, b))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(125)

#                                             Занятие № 9

# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 15))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8:
#             return True
#         else:
#             if len(password) < 8:
#                 print('Количество символов слишком маленькое')
#     else:
#         print('Недопустимые символы')
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Это надежный пароль')
# else:
#     print('Это не надежный пароль')


# def get_sum(a=4, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# s = 2
# print(get_sum(c=s))


# def symbol(sim=20, sign='-'):
#     for i in range(sim):
#         print(sign, end='')
#     print()
#
#
# symbol(10, '+')
# symbol(5, '*')
# symbol(15, '#')
# symbol(7)
# symbol()


# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print('Сумма нечетных цифр:')
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, False))

# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#     print('*' * 20)
#
#
# display_info('Ira', 20)
# display_info(20, 'Ira')
# display_info(age=23, name='Igor')

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
# print(id(lt1))
# print(id(lt2))

# lt1 = 5
# lt2 = 5
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # True
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))

# s = 'Hello '
# print(s)
# print(id(s))
# s += 'World'  # s = s + 'World'
# print(s)
# print(id(s))
# # s[1] = 'a'
# # s[1:2] = 'a'
# # s = s[:1] + s + s[2:]
# s = s[1:-1]
# print(s)
# print(id(s))

# a = 5
# b = 5
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print('Внутри функции:', n, '=', id(n))
#     n += 1
#     print('После изменения:', n, '=', id(n))
#     return n
#
#
# x = 1
# print(x, '=', id(x))
# x = add_numbers(x)
# print(x, '=', id(x))


# def add_numbers(n):
#     print('Внутри функции:', n, '=', id(n))
#     # n += [4]
#     n = n + [4]
#     print('После изменения:', n, '=', id(n))
#     return n
#
#
# x = [1, 2, 3]
# print(x, '=', id(x))
# x = add_numbers(x)
# print(x, '=', id(x))

# типы данных:
# изменяемые: список (list)
# неизменяемые: число (int), строка (str), вещественное число(float), булевые значение (bool)

#                                             Занятие № 10

# Картеж (tuple) - это неизменяемая структура данных, которая по своему подобию очень похожа на список.
# Картеж - неизменяемый список. Или списки доступные только для чтения. Состоит из элементов, разделенных запятыми и
# заключенных в круглые скобки.

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 5, 6, 7, 8)
# print(a)
# print(type(a))
# b = tuple((1, 5, 6, 7, 8))
# print(b)
# print(type(b))
# q = 1, 2, 3, 'w'   # упаковка картежа
# t = (1,)
# print(type(q))
# print(type(t))
# t1 = tuple('hello')
# print(t1)
# print(t1[1])
# print(t1[1:3])
# t1[1] = 'i'

# s1 = tuple(int(input('-> ')) for i in range(5))
# print(s1)

# s = input('-> ')
# print(tuple(s))
# import random

# mas = [random.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)

# mas = tuple(random.randint(0, 100) for i in range(10))
# print(mas)

# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
# if 'e' in t3:
#     print(t3.index('e'))
# else:
#     print('Такого символа нет')
# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(8):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # распаковка картежа
# print(x, y, z)
# print(type(x))
# print(type(t))

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# print(user)
# print(user[0])
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))

# countries = (
#     ('Германия', 20.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, 'население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'население =', city_population)

# Множества (set) - неупорядоченная коллекция, которая хранит только уникальные значения

# {}
# set()

# s = {4, 7, 8, 9, 4, 2, 4, 2, 4}
# print(type(s))
# print(len(s))
# print(s)

# s = set('hello')
# print(s)

# c = [1, 5, 4, 2, 2, 6, 4]
# s = set(c)
# print(s)
# c = list(s)
# print(c)
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(el):
#     st = set(el)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print('green' in t)
# for i in t:
#     print(i)

# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else i(False) for i in последовательность}
# {i(True) if условие else i(False) for i in последовательность if условие}

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
