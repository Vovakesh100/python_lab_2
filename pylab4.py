import re
import os

# далаем файл с примерными данными
if not os.path.exists('text.txt'):
    with open('text.txt', 'w') as file:
        file.write("""email-адреса: example@mail.com, test123@gmail.com.
        Номера телефонов: +7-123-456-78-90, +7-987-654-32-10.
        Слова с заглавной буквы: Москва, Программирование, Python.
        Другое слово: Hello World!""")

with open('text.txt', 'r') as file:
    text = file.read()

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)

# поиск с заглавной буквы
capital_words = re.findall(r'\b[A-ZА-Я][a-zа-я]*\b', text)

# сохраняем в отедлные файлы 
with open('emails.txt', 'w') as f:
    f.write('\n'.join(emails))

with open('phones.txt', 'w') as f:
    f.write('\n'.join(phones))

with open('capital_words.txt', 'w') as f:
    f.write('\n'.join(capital_words))

# Вывод результатов в консоль
print("Найденные email-адреса:", emails)
print("Найденные номера телефонов:", phones)
print("Найденные слова с заглавной буквы:", capital_words)
