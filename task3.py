import math_operations

a = float(input("введите первое число: "))
b = float(input("введите второе число: "))

print(f"сумма: {math_operations.add(a, b)}")
print(f"разность: {math_operations.subtract(a, b)}")
print(f"произведение: {math_operations.multiply(a, b)}")
print(f"деление: {math_operations.divide(a, b)}")