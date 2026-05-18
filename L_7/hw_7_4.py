
def common_elements():

    # 1. Створюю список чисел, котрі кратні 3 за допомогою генератора
    multiples_of_3 = [num for num in range(100) if num % 3 == 0]

    # 2. Створюю список чисел, котрі кратні 5 за допомогою генератора
    multiples_of_5 = [num for num in range(100) if num % 5 == 0]

    # 3. Перетворюю списки на множини
    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)

    # 4. Знаходжу перетин множин (спільні елементи)
    result_set = set_3 & set_5

    # 5. Повертаю отриману множину
    return result_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Результат роботи функції:", common_elements())
print("Перевірку assert пройдено успішно!")
