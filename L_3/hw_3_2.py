
my_list = [12, 3, 4, 10]
# my_list = [1]
# my_list = []
# my_list = [12, 3, 4, 10, 8]

if len(my_list) > 1:
    last_element = my_list.pop()
    my_list.insert(0, last_element)

print(my_list)

# Результат_1: [10, 12, 3, 4]
# Результат_2: [1]
# Результат_3: []
# Результат_4: [8, 12, 3, 4, 10]
