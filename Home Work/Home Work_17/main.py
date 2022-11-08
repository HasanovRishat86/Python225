# Задача № 1

# # s = 'I am learning Python. hello, WORLD!'  # введенная строка
#
# s = input('Введите строку: ')
# ind1 = s.index('h')
# ind2 = s.rindex('h')
# print(s[:ind1] + s[ind2 + 1:])

# Задача № 2

# # s = 'I am learning Python. hello, WORLD!'  # введенная строка
#
# s = input('Введите строку: ')
# ind1 = s.index('h')
# ind2 = s.rindex('h')
# print(s[:ind1] + s[ind2:ind1:-1] + s[ind2 + 1:])

# Задача № 3

# s = input('Строка: ')
# zam = input('Ее заменяемая подстрока: ')
# zam_new = input('Новая подстрока: ')
# print(s.replace(zam, zam_new))

# Задача № 4

# s = """Ежевику для ежат
# Приносили два ежа.
# Ежевику еле-еле
# Ежат возле ели съели"""
#
# up = s.count('Е')
# down = s.count(" е")
# e = up + down
# print("Количество слов:", e)
