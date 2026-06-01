
def generate_cube_numbers(end):
    # Починаю з числа 2
    current_number = 2

    while True:
        # Обчислюю куб поточного числа
        cube = current_number ** 3

        # Якщо куб більше за вказану межу (end), виходжу з генератора
        if cube > end:
            return

        # Інакше "віддаю" куб числа і призупиняю функцію до наступного виклику
        yield cube

        # Переходжу до наступного числа
        current_number += 1

# Блок перевірок
from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print("Всі тести пройдено успішно!")
