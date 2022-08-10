# Задача № 1

# n = [int(input('-> ')) for i in range(int(input('n = ')))]
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i], end=' ')

# Задача № 2
# n = [int(input('-> ')) for i in range(int(input('n = ')))]
# a = n[0]
# for i in range(len(n)):
#     if n[i] > a:
#         print(n[i], end=' ')
#     a = n[i]

# Задача № 3
# for i in range(1, 8):
#     print('*' * i)

# Задача № 4
# for i in range(7, 0, -1):
#     print('*' * i)

# Задача № 5
# h = int(input('Введите размер поля: '))
# x = int(input('Введите количество символов: '))
# n = 0
# for i in range(h):
#     for j in range(x):
#         for m in range(h):
#             if m % 2 == 0:
#                 if i % 2 == 0:
#                     while n < x:
#                         print('*', end=' ')
#                         n += 1
#                     n = 0
#                 if i % 2 == 1:
#                     while n < x:
#                         print(' ', end=' ')
#                         n += 1
#                     n = 0
#             if m % 2 == 1:
#                 if i % 2 == 1:
#                     while n < x:
#                         print('*', end=' ')
#                         n += 1
#                     n = 0
#                 if i % 2 == 0:
#                     while n < x:
#                         print(' ', end=' ')
#                         n += 1
#                     n = 0
#         print()


