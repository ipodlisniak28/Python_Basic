
# Конвертер із числа в дату
# Розкоментовую приклад та закоментую рядок з input() нижче.

# Приклад 1: Очікуваний результат: 0 днів, 00:00:00
# total_seconds = 0

# Приклад 2: Очікуваний результат: 2 дні, 14:28:50
# total_seconds = 224930

# Приклад 3: Очікуваний результат: 5 днів, 09:31:29
# total_seconds = 466289

# Приклад 4: Очікуваний результат: 11 днів, 00:00:00
# total_seconds = 950400

# Приклад 5: Очікуваний результат: 14 днів, 00:00:00
# total_seconds = 1209600

# Приклад 6: Очікуваний результат: 22 дні, 00:00:00
# total_seconds = 1900800

# Приклад 7: Очікуваний результат: 99 днів, 23:59:59
# total_seconds = 8639999

# Приклад 8: Очікуваний результат: 0 днів, 06:14:53
# total_seconds = 22493

# Приклад 9: Очікуваний результат: 91 день, 23:59:59
# total_seconds = 7948799

# Основний варіант для роботи програми через консоль:
total_seconds = int(input("Введіть кількість секунд (від 0 до 8640000): "))

# Константи для обчислень
SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60

# Розрахунок днів, годин, хвилин та секунд
days, remainder = divmod(total_seconds, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

# Визначення правильної форми слова "день"
if days % 100 in [11, 12, 13, 14]:
    days_word = "днів"
elif days % 10 == 1:
    days_word = "день"
elif days % 10 in [2, 3, 4]:
    days_word = "дні"
else:
    days_word = "днів"

# Форматування виведення за допомогою zfill(2)
hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

# Виведення фінального результату
print(f"{days} {days_word}, {hours_str}:{minutes_str}:{seconds_str}")
