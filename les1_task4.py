# 4. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят, и сколько между ними находится букв.

from string import ascii_lowercase

print('Введите два символа англ. алфавита:\n')
S1 = input('Первый символ: \n').lower()
S2 = input('Второй символ: \n').lower()

X1 = ascii_lowercase.find(S1)
X2 = ascii_lowercase.find(S2)
d = len(ascii_lowercase[X1+1:X2])

print(f'Англ. алфавит: {" ".join(ascii_lowercase)}')
print(f'Порядковый номер символа {S1} равен {X1}\n'
      f'Порядковый номер символа {S2} равен {X2}\n'
      f'Между символами {S1} и {S2} находятся {d} букв\n')
