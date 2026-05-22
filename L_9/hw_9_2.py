
def difference(*args):

    # Перевіряю, чи передані аргументи взагалі
    if not args:
        return 0

    # Знаходжу найбільше та найменше значення
    maximum = max(args)
    minimum = min(args)

    # Знаходжу різницю та округлюю її до 2 знаків після коми
    result = maximum - minimum
    return round(result, 2)

# Тести
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'

print('OK')
