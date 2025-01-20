from math import ceil

def square(side):
    side = ceil(side)
    return side * side

n = float(input('Введите число: '))
result = square(n)
print(f"Площадь {n}: {result}")