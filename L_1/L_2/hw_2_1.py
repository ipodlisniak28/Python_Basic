
# --- Завдання 1: Квадрат числа ---
number = float(input("Введіть число: "))
square = number ** 2

print(f"Квадрат числа: {square}")


# --- Завдання 2: Середнє трьох чисел ---
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

average = (num1 + num2 + num3) / 3

print(f"Середнє: {average}")


# --- Завдання 3: Перетворення хвилин у години ---
total_minutes = int(input("Введіть кількість хвилин: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours} години {minutes} хвилин")


# --- Завдання 4: Розрахунок знижки ---
price = float(input("Введіть ціну: "))
discount_percent = float(input("Введіть знижку (%): "))

discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

print(f"Ціна зі знижкою: {final_price}")


# --- Завдання 5: Остання цифра числа ---
number_to_check = int(input("Введіть число: "))
last_digit = number_to_check % 10

print(f"Остання цифра: {last_digit}")


# --- Завдання 6: Периметр прямокутника ---
length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))

perimeter = 2 * (length + width)

print(f"Периметр: {perimeter}")


# --- Завдання 7: Виведення 4-значного числа в стовпчик ---
four_digit_num = int(input("Введіть 4-х значне число: "))

# Використовуємо цілочисельне ділення та залишок
digit1 = four_digit_num // 1000
digit2 = (four_digit_num // 100) % 10
digit3 = (four_digit_num // 10) % 10
digit4 = four_digit_num % 10

# Виведення кожної цифри окремим принтом
print(digit1)
print(digit2)
print(digit3)
print(digit4)
