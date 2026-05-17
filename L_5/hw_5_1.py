
import keyword
import string

# Отримую рядок від Користувача
user_input = input("Введіть ім'я змінної: ")

# Перевіряю всі умови за чергою
if user_input == "":
    result = False

# 1. Перевірка, чи не є рядок зареєстрованим ключовим словом
elif user_input in keyword.kwlist:
    result = False

# 2. Перевірка, чи не починається рядок з цифри
elif user_input[0].isdigit():
    result = False

# 3. Перевірка на два підкреслення підряд
elif "__" in user_input:
    result = False

# 4. Перевірка на великі літери (за умовою, якщо рядок не дорівнює самому собі в нижньому регістрі)
elif user_input != user_input.lower():
    result = False

# 5. Перевірка на пробіли та знаки пунктуації
else:
    # Лайфхак: видаляю всі "_" і перевіряю, що залишилося
    clean_str = user_input.replace("_", "")

    # а) Якщо після видалення "_" рядок став порожнім (наприклад, було лише "_"), то він валідний.
    # б) Якщо він не порожній, метод .isalnum() перевірить, чи складається він ТІЛЬКИ з літер та цифр.
    # в) Якщо там залишився пробіл або знак пунктуації (string.punctuation), .isalnum() поверне False.

    if clean_str != "" and not clean_str.isalnum():
        result = False
    else:
        result = True

# Виведення лише булінгових значень True або False
print(result)
