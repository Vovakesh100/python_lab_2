import re
import os

# создаём файл text.txt с примерами дат
if not os.path.exists('text.txt'):
    with open('text.txt', 'w') as file:
        file.write("""01.01.2023 — Новый год
        15.05.2024 — День программиста
        31.12.2024 — Канун Нового года
        Некорректные даты: 99.99.9999, 1.1.2025""")

with open('text.txt', 'r') as file:
    text = file.read()

# поиск дат в формате DD.MM.YYYY
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

# преобразование формата дат
converted_dates = ["-".join(date.split('.')[::-1]) for date in dates]

# сохранение результатов в dates.txt
with open('dates.txt', 'w') as file:
    file.write('\n'.join(converted_dates))

# сортировка дат по возрастанию 
sorted_dates = sorted(converted_dates, key=lambda x: tuple(map(int, x.split('-'))))

# Вывод результатов
print("Найденные даты:", dates)
print("Преобразованные даты:", converted_dates)
print("Отсортированные даты:", sorted_dates)
