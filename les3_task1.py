""""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
array1 = list(range(2, 100))
array2 = list(range(2, 10))
results_list = [[] for _ in range(2, 10)]

i = 0
j = 0

while i <= len(array1) - 1:
    while j <= len(array2) - 1:
        if array1[i] % array2[j] == 0:
            results_list[j].append(array1[i])
        j = j + 1
    j = 0
    i = i + 1

for i in range(8):
    print(f'Элементы, кратные {array2[i]} ->> {results_list[i]}. Всего их {len(results_list[i])}')

