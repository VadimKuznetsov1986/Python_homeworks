# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

num = int(input('Введите N: '))
lst = []
for i in range(-abs(num), abs(num) + 1):
    lst.append(i)
print(lst)
mult = 1
with open('position.txt', 'r') as data:
    for i in data:
        if int(i) > len(lst) - 1 or int(i) < -len(lst):
            print('Неверный индекс')
            exit()
        mult *= lst[int(i)]
print(f'Произведение элементов = {mult}')

