
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Відкриваю і читаю вихідний файл
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Очищую від тегів
    text_without_tags = ""
    inside_tag = False  # Цей "прапорець" показує, чи знаходжусь Я всередині тегу

    # Перебираю кожен символ у тексті
    for char in html:
        if char == '<':
            inside_tag = True  # Зайшов в тег, перестаю записувати символи
        elif char == '>':
            inside_tag = False  # Вийшов з тегу, можна знову записувати
        elif not inside_tag:
            text_without_tags += char  # Записую символ, тільки якщо він не в тегу

    # Прибираю рядки, у яких немає інформації
    cleaned_lines = []

    # Розбиваю текст на окремі рядки
    for line in text_without_tags.split('\n'):
        # Метод strip() видаляє пробіли. Якщо після цього рядок не порожній — він мені буде потрібен
        if line.strip():
            # Додаю очищений від зайвих пробілів по краях рядок
            cleaned_lines.append(line.strip())

    # Збираю всі корисні рядки назад у текст (з переносом на новий рядок)
    final_text = '\n'.join(cleaned_lines)

    # Записую результат у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)

# Викликаю функцію для перевірки
# delete_html_tags('draft.html')
