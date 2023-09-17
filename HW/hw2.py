# 2.1 Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
# health = int(input('Введите уровень здоровья: '))
# print(health > 0)

#2.2 Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”, а иначе - “Нечетное”
# 1)
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
# 2)
# number = int(input('Введите число: '))
# if number % 2 :
#     print("Нечетное")
# else:
#     print("Четное")

#2.3 Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
# которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# year = int(input('Введите год: '))
# if year > 0:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("Високосный")
#     else:
#         print("Невисокосный")
# else:
#     print("Введите корректный год")

#2.4 Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()
# 1)
# text = input('Введите текст: ')
# n = int(input('Введите число повторений: '))
# print((text + "\n") * n)
# 2)
# text = input('Введите текст: ')
# n = int(input('Введите число повторений: '))
# i = 0
# while i < n:
#     print(text)
#     i += 1
# 3)
# text = input('Введите текст: ')
# n = int(input('Введите число повторений: '))
# for i in range(n):
#     print(text)

#2.5 Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате:
# {num1} {operator) {num2) = {result}
# num1 = input('Введите первое число: ')
# num2 = input('Введите второе число: ')
# operator = input('Введите +, -, *, **, /, // или % : ')
# result = 0
# if operator in "+-**//%" and num1.isdigit() and num2.isdigit():
#     if int(num2) == 0 and (operator == "/" or operator == "//" or operator == "%"):
#         print("You can't divide by zero")
#     else:
#         if operator == "+":
#             result = {int(num1) + int(num2)}
#         elif operator == "-":
#             result = {int(num1) - int(num2)}
#         elif operator == "*":
#             result = {int(num1) * int(num2)}
#         elif operator == "**":
#             result = {int(num1) ** int(num2)}
#         elif operator == "/":
#             result = {int(num1) / int(num2)}
#         elif operator == "//":
#             result = {int(num1) // int(num2)}
#         else:
#             result = {int(num1) % int(num2)}
#         print(f"{num1} {operator} {num2} = {result}")
# else:
#     print("Enter valid data")
