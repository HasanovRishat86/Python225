def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


a = [1, 2, 3]
b = [9, 12, 33, 54, 105]
c = ['с', 'л', 'о', 'н']
print('Исходные данные:')
print(a)
print(b)
print(c)
print('Результат:')
print(change(a))
print(change(b))
print(change(c))


