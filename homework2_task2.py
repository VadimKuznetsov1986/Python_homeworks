# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N

num = int(input('Введите число: '))
f = 1
lst = []
for i in range(1, num + 1):
    f *= i
    lst.append(f)
print(lst)

