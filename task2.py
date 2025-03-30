try:
    num1 = float(input("введите делимое: "))
    num2 = float(input("введите делитеель: "))
    res = num1 / num2
except ZeroDivisionError:
    print("ошибка: деление на ноль")
except ValueError:
    print("ошибка: это не число")
except Exception as e:
    print(f"неизвестная ошибка: {e}")
else:
    print(f"Результат деления {num1} на {num2} равен {result}")