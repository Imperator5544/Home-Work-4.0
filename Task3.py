"""Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
"""

input_string = input("Enter a string: ")

search_word = input("Enter a word to search for: ")
replace_word = input("Enter a replacement word ")

words = input_string.split()

for i in range(len(words)):

    if words[i] == search_word:
        words[i] = replace_word

result_string = ' '.join(words)

print("The resulting string:", result_string)