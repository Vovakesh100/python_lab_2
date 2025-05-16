def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Ошибка: Деление на ноль"
import math_operations as mo

a, b = 40, 10
print(f"Сложение: {mo.add(a, b)}")
print(f"Вычитание: {mo.subtract(a, b)}")
print(f"Умножение: {mo.multiply(a, b)}")
try:
    print(f"Деление: {mo.divide(a, b)}")
except ValueError as e:
    print(e)
