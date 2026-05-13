
# Найпростіший калькулятор

print("Вітаю у Python-Калькуляторі!")

try:
    # Просимо користувача почергово ввести дані
    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть математичну дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    # Перевіряємо, яку дію обрав користувач і виконуємо обчислення
    if operation == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")

    elif operation == '/':
        # Головна умова ДЗ: перевірка ділення на нуль
        if num2 == 0:
            print("Помилка: Ділення на нуль неможливе!")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")

    else:
        print("Помилка: Невідома дія. Будь ласка, використовуйте тільки +, -, * або /.")

except ValueError:
    # Відловлюємо помилку, якщо ввели текст замість числа
    print("Помилка: Будь ласка, вводьте лише числа!")
