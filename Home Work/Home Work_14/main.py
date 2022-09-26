from math import pi


def figure(figure_type, **kwargs):
    if figure_type == 'rhombus':
        return kwargs['d1'] * kwargs['d2'] / 2
    if figure_type == 'square':
        return kwargs['a'] ** 2
    if figure_type == 'trapezoid':
        return 0.5 * (kwargs['a'] + kwargs['b']) * kwargs['h']
    if figure_type == 'circle':
        return pi * kwargs['r'] ** 2
    else:
        return 'invalid data'

print(figure(figure_type='rhombus', d1=10, d2=8))
print(figure(figure_type='square', a=5))
print(figure(figure_type='trapezoid', a=12, b=3, h=6))
print(figure(figure_type='circle', r=18))
print(figure(figure_type='unknown', a=1, b=2, c=3))
