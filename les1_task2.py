#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

print('Ввод координат первой точки:')
x1 = int(input('Введите x1: \n'))
y1 = int(input('Введите y1: \n'))

print('Ввод координат второй точки:')
x2 = int(input('Введите x2: \n'))
y2 = int(input('Введите y2: \n'))

k = (y2 - y1) / (x2 - x1)
b = y1 - k*x1

print(f'Имеем уравнение прямой:\n y = {k:.2f}x + {b:.2f}')

