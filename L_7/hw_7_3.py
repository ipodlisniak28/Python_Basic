
def second_index(text, some_str):
    # Крок 1: Шукаю індекс першого входження
    first_index = text.find(some_str)

    # Якщо перший рядок взагалі не знайдено, то й другого точно немає
    if first_index == -1:
        return None

    # Крок 2: Шукаю друге входження, починаючи пошук ОДРАЗУ після першого індексу
    # Додаю 1 до first_index, щоб не знайти знову ту саму букву/підрядок
    second_idx = text.find(some_str, first_index + 1)

    # Якщо другого входження немає, метод find() поверне -1
    if second_idx == -1:
        return None

    # Якщо знайшовся — повертаю цей індекс
    return second_idx

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
