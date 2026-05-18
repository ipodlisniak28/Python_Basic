
def add_one(some_list):
    # 1. Перетворюю список цифр в один рядок
    number_str = ""
    for digit in some_list:
        number_str += str(digit)

    # 2. Перетворюю рядок у число і додаю одиницю
    total_sum = int(number_str) + 1

    # 3. Перетворюю отриману суму назад у список окремих цифр
    result_list = []
    for char in str(total_sum):
        result_list.append(int(char))

    return result_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")