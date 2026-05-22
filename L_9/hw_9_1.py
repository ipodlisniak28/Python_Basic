
def popular_words(text, words):

    # Переводжу весь текст у нижній регістр і розбиваю його на список окремих слів
    text_words = text.lower().split()

    # Створюю порожній словник для збереження результатів
    result = {}

    # Проходжуся циклом по кожному шуканому слову
    for word in words:
        # Метод count() рахує, скільки разів точне слово зустрічається у списку
        # Якщо слова немає, count() автоматично поверне 0
        result[word] = text_words.count(word)

    return result

# Перевірка (assert):
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
