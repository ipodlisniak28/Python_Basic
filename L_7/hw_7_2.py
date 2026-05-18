
def correct_sentence(text):
    # 1. Роблю першу літеру великою, а весь інший рядок додаю без змін
    text = text[0].upper() + text[1:]

    # 2. Перевіряю, чи закінчується рядок крапкою.
    # Якщо ні — додаю її в кінець.
    if not text.endswith('.'):
        text += '.'

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
