"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

array = [random.randint(1, 100) for _ in range(10)]
print(f'Был введен список: {array}')

i = 0
var_max = i
var_min = i

while i <= len(array) - 1:
    if array[i] > array[var_max]:
        var_max = i
    elif array[i] < array[var_min]:
        var_min = i
    i = i + 1

print(f'Макс элемент: {array[var_max]}\n'
      f'Мин. элемент: {array[var_min]}')
foo = array[var_max]
array[var_max] = array[var_min]
array[var_min] = foo

print(f'Массив после изменений: {array}')
