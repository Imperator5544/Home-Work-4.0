"""Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
"""

input_string = input("Enter a string: ")

search_word = input("Enter a word to search for: ")

replace_word = input("Enter a replacement word ")

result_string = input_string.replace(search_word, replace_word)

print("The resulting string:", result_string)

