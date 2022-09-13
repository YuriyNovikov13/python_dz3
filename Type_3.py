# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
a = [1.1, 1.2, 3.1, 5, 10.01]
z = []


def fractional(x, y):
    for i in range(int(len(x))):
        b = float(x[i])//1
        c = round(float(x[i])-b, 2)
        if c != 0.0:
            y.append(c)
    return y


def max_frac(x):
    max_f = float(x[0])
    for i in range(int(len(x))):
        if max_f < float(x[i]):
            max_f = float(x[i])
    return max_f


def min_frac(x):
    min_f = float(x[0])
    for i in range(int(len(x))):
        if min_f > float(x[i]):
            min_f = float(x[i])
    return min_f


print(f'максимальное значение дробной части -> {max_frac(fractional(a, z))}')
print(f'минимальное значение дробной части -> {min_frac(fractional(a, z))}')
print(f'разница между макс и мин значениями дробной части -> {max_frac(fractional(a, z)) - min_frac(fractional(a, z))}')
