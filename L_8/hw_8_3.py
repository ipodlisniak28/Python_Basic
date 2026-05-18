
def find_unique_value(some_list):
    # Проходжу по кожному елементу списку
    for item in some_list:
        # Якщо елемент зустрічається в списку рівно 1 раз, повертаю його
        if some_list.count(item) == 1:
            return item

# Перевірка працездатності коду за допомогою 'Test1', 'Test2', 'Test3':
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")
