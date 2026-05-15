
# Список із 3 елементів

import random

# Приклад 1:
original_list = [1, 2, 3, 4, 5, 6, 7, 9]

# Приклад 2:
# original_list = [1, 1, 2, 1]

# Приклад 3:
# original_list = [6, 3, 7]

list_length = random.randint(3, 10)
original_list = []
for _ in range(list_length):
    random_number = random.randint(1, 10)
    original_list.append(random_number)

# Вибираю: перший [0], третій [2] та другий з кінця [-2] для списку з п.1
new_list = [original_list[0], original_list[2], original_list[-2]]

# Фінальний вивід у консоль
print(f"{original_list} == {new_list}")
