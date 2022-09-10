#                                  Задача № 1

# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 60, 6: 60}
# dict_all = {**dict1, **dict2, **dict3}
# print(dict_all)

#                                  Задача № 2

# d = {'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
# for k in d:
#      print(k)
#      for i in d[k]:
#           print('\t', i, ': ', d[k][i], sep='')

#                                  Задача № 3

col = int(input('Введите количество студентов: '))
d = dict()
j = 1
summ = 0
for i in range(col):
    print(j, end='')
    name = str(input('-й студент: '))
    ball = int(input('Балл: '))
    summ = summ + ball
    # d[name].append(ball)
    j += 1
sred = summ / col
print('Средний балл:', sred, '. Студенты с баллом выше среднего:')
for k, v in d:
    if d[k][v] > sred:
        print(d[k])




