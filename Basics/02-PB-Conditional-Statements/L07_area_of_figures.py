# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята
# лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle
# или triangle).
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му
# и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

from math import pi

figure = str(input())

area = 0

if figure == 'square':
    a = float(input())
    area = a*a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a*b
    print(f'{area:.3f}')
elif figure == 'circle':
    r = float(input())
    area = r*r*pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a*h/2
    print(f'{area:.3f}')