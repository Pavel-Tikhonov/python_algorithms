#3. Написать программу, которая генерирует в указанных пользователем границах:
#c. случайный символ.

from random import random
from string import ascii_lowercase

print('Генерация случайного символа анг. алфавита из диапазона.\n'
      'Введите нижнюю и верхнюю границу диапазона:')
Smin = input('Нижняя граница: \n').lower()
Smax = input('Верхняя граница: \n').lower()

Xmin = ascii_lowercase.find(Smin)
Xmax = ascii_lowercase.find(Smax)

R = random()
X = (Xmax - Xmin) * R + Xmin
X = round(X)
S = ascii_lowercase[X]

print(f'Англ. алфавит: {" ".join(ascii_lowercase)}')
print(f'Случайное символ англ. алфавита из диапазона от {Smin} до {Smax} - есть {S}')

