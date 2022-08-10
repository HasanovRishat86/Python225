# from random import randint

# Задача № 1

# a = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# otr = 0
# for row in a:
#     for x in row:
#         print(x, end='\t\t')
#         if x < 0:
#             otr += 1
#     print()
# print('Количество отрицательных элементов:', otr)

# Задача № 2

# a = [[randint(0, 4) for x in range(3)] for y in range(4)]
# pr = 1
# for row in a:
#     for x in row:
#         print(x, end='\t\t')
#         if x > 0:
#             pr *= x
#     print()
# print('Произведение ненулевых элементов:', pr)

# Задача № 3 (дополнительная)

# a = [[randint(0, 10) for x in range(6)] for y in range(6)]
# for row in a:
#     for x in row:
#         print(x, end='\t\t')
#     print()
# b = [randint(0, 10) for x in range(6)]
# print(b)
# i = 0
# for row in range(len(a)):
#     i += 1
#     for x in range(len(a[row])):
#         if i % 2 == 1:
#             a[row][x] = b[x]
# for row in a:
#     for x in row:
#         print(x, end='\t\t')
#     print()

