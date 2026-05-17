
# Початкове значення змінної, щоб цикл запустився вперше
restart = 'yes'

while restart == 'yes' or restart == 'y':
    # 1. Запит чисел та операції у Користувача
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    # 2. Блок обчислень
    if operator == '+':
        result = num1 + num2
        print(f"Результат: {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"Результат: {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"Результат: {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {result}")
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Помилка: невідома операція!")

    # 3. Запит на продовження роботи
    user_choice = input("\nБажаєте виконати ще одне обчислення? (yes/y): ")

    # Обробляю рядок: прибираю пробіли по боках та переводжу в нижній регістр
    restart = user_choice.strip().lower()

print("\nРоботу калькулятора завершено. Гарного дня!")
