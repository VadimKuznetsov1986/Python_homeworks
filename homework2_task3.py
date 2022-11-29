# Задайте словарь из n чисел последовательности (1 + (1/n))^n и
# выведите на экран их сумму

num = int(input('Введите число: '))
lst = {}
total = 0
for i in range(1, num + 1):
    lst[i] = round((1 + (1 / i)) ** i, 3)
    total += lst[i]
print(lst)
print(f'Сумма = {round(total, 3)}')

