"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Введите количество элементов ряда: '))

n0 = -2
delta = -0.5
my_sum = 0
my_list = []

for i in range(n):
    n_nxt = n0 * delta
    my_list.append(n_nxt)
    my_sum += n_nxt
    n0 = n_nxt

print(f'Вы ввели {n}\n'
      f'Составлен соответствующий ряд:\n'
      f'{my_list}\n'
      f'Сумма ряда равна {my_sum}')

