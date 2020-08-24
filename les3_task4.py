"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

array = [random.randint(1, 10) for _ in range(10)]
print(f'Был введен список: {array}')

num = array[0]
i = 0
j = 1
count_max = 1

while i <= len(array) - 2:
    count = 1
    while j <= len(array) - 1:
        if array[i] == array[j]:
            count = count + 1
        j = j + 1
    if count > count_max:
        count_max = count
        num = array[i]
    i = i + 1
if count_max > 1:
    print(f'Чаще всего встречается {num} - {count_max} раза.')
else:
    print('Каждое число уникально')

