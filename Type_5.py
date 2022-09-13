# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  
def fib1(n):
    f1 = 0
    f2 = 1
    for i in range(0, n):
        f1, f2 = f2, f1 + f2
    return f2    

def fib2(n):
    f1 = 0
    f2 = 1
    for i in range(0, n):
        f1, f2 = f2, f1 + (-f2)
    return f2 

lst1 = [0, ]
n = int(input('Fibonnacci = '))
for i in range(n):
    lst1.append(fib1(i))


lst2 = []
for i in range(n):
    lst2.append(fib2(i))

  

lst3 = []
for i in range(n):
    b = int(lst2[-i-1])
    lst3.append(b)

for i in range(n+1):
    lst3.append(lst1[i])
print(lst3)
