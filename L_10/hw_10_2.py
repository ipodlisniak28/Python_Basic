
def first_word(text):
    """ Пошук першого слова """
    # 1. Замінюю всі крапки та коми на пробіли.
    # Це дозволить мені ізолювати слова одне від одного.
    clean_text = text.replace('.', ' ').replace(',', ' ')

    # 2. Розбиваю рядок на список слів.
    # Метод split() без аргументів автоматично ігнорує будь-яку кількість
    # пробілів підряд і розділяє лише по існуючих словах.
    words = clean_text.split()

    # 3. Повертаю перший елемент списку (це і є моє перше слово!)
    return words[0]

# Перевірка
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')
