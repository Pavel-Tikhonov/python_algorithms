#7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
#В соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

n = int(input('Введите год: \n'))

if n % 4 == 0:
    if n % 100 == 0:
        print('Год не является високосным')
    else:
        print('Год является високосным')
else:
    if n % 400 == 0:
        print('Год является високосным')
    else:
        print('Год не является високосным')

