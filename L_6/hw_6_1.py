
import string

# Діапазон букв

# Приклад 1: Очікуваний результат: abc
# user_input = "a-c"

# Приклад 2: Очікуваний результат: a
# user_input = "a-a"

# Приклад 3: Очікуваний результат: stuvwxyzABCDEFGH
# user_input = "s-H"

# Приклад 4: Очікуваний результат: abcdefghijklmnopqrstuvwxyzA
user_input = "a-A"

# а) Отримую введення від Користувача
user_input = input("Введіть дві літери через дефіс: ")

# б) Розділяю рядок по дефісу на початкову та кінцеву літери
start_char, end_char = user_input.split('-')

# в) Знаходжу порядкові номери (індекси) літер у стандартному наборі ascii_letters
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char)

# г) Беру зріз рядка від start_index до end_index включно (+1)
result = string.ascii_letters[start_index:end_index + 1]

# Виводжу результат
print(result)
