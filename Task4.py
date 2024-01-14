"""
 Дано рядок. (зробити зрізи)

- Спершу виведіть третій символ цього рядка.

- У другому рядку виведіть передостанній символ цього рядка.

- У третьому рядку виведіть перші п'ять символів цього рядка.

- У четвертому рядку виведіть весь рядок, крім двох останніх символів.

- У п'ятому рядку виведіть усі символи з парними індексами
(вважаючи, що індексація починається з 0, тому символи виводяться з першого).

- У шостому рядку виведіть усі символи з непарними індексами, тобто,
починаючи з другого символу рядка.

- У сьомому рядку виведіть усі символи у зворотному порядку.

- У восьмому рядку виведіть усі символи рядка через один у зворотному порядку,
починаючи з останнього.

- У дев'ятому рядку виведіть довжину цього рядка.
"""

input_string = "Я прийшов додому. Попити самогону"
print(input_string[2])

input_string = "Їхав я додому з роботи, щоб не зазнавати турботи."
print(input_string[-2])

input_string = "Я їду до тебе."
print(input_string[:5])

input_string = "Я хочу кави."
print(input_string[:-2])

input_string = "I go to the сinema"
print(input_string[::2])

input_string = "I am carrying 12 kittens."
print(input_string[1::2])

input_string = "I love rock&roll!"
print(input_string[::-1])

input_string = "Carry on Wayward Son"
print(input_string[::-2])

input_string = "I'm on the highw. On the highway to hell. Highway to hell. I'm on the highway to hell"
print(len(input_string))