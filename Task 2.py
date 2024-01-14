"""
Користувач вводить з клавіатури рядок та символ для пошуку.
Порахуйте скільки разів у рядку зустрічається потрібний символ.
Отримане число виведіть на екран.
"""

input_string = input("Enter a string: ")

search_char = input("Enter a character to search for: ")

char_count = 0

for char in input_string:

    if char == search_char:
        char_count += 1

print(f"Number of occurrences of the character '{search_char}': {char_count}")