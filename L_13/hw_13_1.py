
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Відкриваю файл для читання
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # 1. Очищення від HTML-тегів
    # Поки в тексті є символи '<' та '>'
    while '<' in html and '>' in html:
        start_index = html.find('<')
        end_index = html.find('>', start_index)

        # Якщо знайшов коректну пару символів
        if start_index != -1 and end_index != -1:
            # Склеюю текст ДО тегу та текст ПІСЛЯ тегу, пропускаючи сам тег
            html = html[:start_index] + html[end_index + 1:]
        else:
            break  # Запобіжник, якщо раптом є '<', але немає '>'

    # Додатково прибираю порожні рядки
    # Розбиваю текст на список рядків
    lines = html.split('\n')
    cleaned_lines = []

    for line in lines:
        # Методом strip() прибираю пробіли по краях.
        # Якщо після цього рядок не порожній, додаю його до списку.
        if line.strip():
            cleaned_lines.append(line.strip())

    # Збираю список назад у єдиний текст, поєднуючи рядки перенесенням
    cleaned_text = '\n'.join(cleaned_lines)

    # Записую у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)

    print(f"Файл успішно очищено! Результат збережено у {result_file}")

# Викликаю функцію
# delete_html_tags('draft.html')
