# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


print('введите список из нескольуих чисел через запятую: ')
new_list = list(input())
arr = list(filter(str.isdigit, new_list))
i = 1
sum_result = 0
while i < len(arr):
    sum_result = sum_result + int(arr[i])
    i += 2
print(f' -> {sum_result}')
