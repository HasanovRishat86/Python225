print('Программа "Калькулятор"')
x = a = b = 0
while x != 9:
    print()
    print('Выберите операцию:')
    print('1 - "r" - применяет унарный минус к операнду')
    print('2 - "+" - сложение')
    print('3 - "-" - вычитание')
    print('4 - "/" - деление')
    print('5 - "*" - умножение')
    print('6 - "%" - деление по модулю (остаток от деления)')
    print('7 - "<" - минимальное из двух чисел')
    print('8 - ">" - максимальное из двух чисел')
    print('9 - для выхода из программы')
    x = input('Введите цифру: ')
    try:
        x = int(x)
    except ValueError:
        print('\nВы выбрали неверную операцию!!!')
        x = 0
    if 1 < x > 9:
        print('\nВы выбрали неверную операцию!!!')
        x = 0
    else:
        if x == 1:
            a = input('Введите число: ')
            try:
                a = float(a)
                print('\nРезультат равен:', a * -1)
            except ValueError:
                input('\nВведены неверные данные!!!')
        elif x != 0:
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            try:
                a = float(a)
                b = float(b)
                if x == 2:
                    print('\nРезультат равен:', a + b)
                if x == 3:
                    print('\nРезультат равен:', a - b)
                if x == 4:
                    print('\nРезультат равен:', a / b)
                if x == 5:
                    print('\nРезультат равен:', a * b)
                if x == 6:
                    print('\nРезультат равен:', a % b)
                if x == 7:
                    if a < b:
                        print('\nМинимальное из двух чисел равно:', a)
                    else:
                        print('\nМинимальное из двух чисел равно:', b)
                if x == 8:
                    if a > b:
                        print('\nМаксимальное из двух чисел равно:', a)
                    else:
                        print('\nМаксимальное из двух чисел равно:', b)
            except ValueError:
                input('\nВведены неверные данные!!!')
            except ZeroDivisionError:
                input('\nНа ноль делить нельзя!!!')
print('Конец программы!')
