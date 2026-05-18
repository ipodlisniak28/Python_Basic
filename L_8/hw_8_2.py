
def is_palindrome(text):
    # Створюю порожній рядок для очищеного тексту
    cleaned_text = ""

    # Проходжу по кожному символу вхідного рядка
    for char in text:
        # Перевіряю, чи є символ літерою або цифрою (ігнорую пунктуацію та пробіли)
        if char.isalnum():
            # Приводжу до нижнього регістру та додаю до свого рядка
            cleaned_text += char.lower()

    # Оптимально перевіряю, чи читається рядок однаково з обох боків
    # Зріз [::-1] — це найефективніший спосіб розгорнути рядок у Python
    return cleaned_text == cleaned_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
