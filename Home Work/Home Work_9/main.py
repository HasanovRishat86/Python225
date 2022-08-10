from math import pi


def rectangle():
    a = float(input('Введите длинну прямоугольника: '))
    b = float(input('Введите ширину прямоугольника: '))
    return a * b


def triangle():
    a = float(input('Введите длинну основания треугольника: '))
    h = float(input('Введите высоту треугольника: '))
    return 0.5 * a * h


def circle():
    r = float(input('Введите радиус: '))
    return 2 * pi * r


print('Выберите фигуру, для нахождения ее площади:')
x = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))
if x == 1:
    print('Площадь прямоугольника: ', round(rectangle(), 2))
elif x == 2:
    print('Площадь треугольника: ', round(triangle(), 2))
elif x == 3:
    print('Площадь круга: ', round(circle(), 2))
else:
    print('Введены некорректные данные!!!')
