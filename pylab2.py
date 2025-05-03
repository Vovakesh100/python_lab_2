def divide_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 / num2
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
    except ValueError:
        print("Ошибка: Введено нечисловое значение")

divide_numbers()
