"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input('Введите число: '))
even = []
uneven = []
print(f'Вы ввели число {num}.')

while num > 0:
    d = num % 10
    if d == 0:
        if num // 10 == 0:
            d = num
    if d != 0:
        if d % 2 == 0:
            even.append(d)
        else:
            uneven.append(d)
    num //= 10

print(f'В вашем числе {len(even)} четных цифр: {even}\n'
      f'и {len(uneven)} нечетных цифр: {uneven}.')
