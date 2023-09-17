# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# result = []
# for i in str(my_list):
#     if str(i).isdigit():
#         result.append(int(i))
# print(result)

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# sum = 0
# list_2 = []
# for i in list_1:
#     if str(i).isdigit():
#         sum += i
#     if str(i).find("a") != -1:
#         list_2.append(i)
# print(sum)
# print(list_2)

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# list3 = ['cat', 'dog', 'horse', 'cow']
# print(list3)
# print(tuple(list3))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input("введите через запятую членов вашей семьи: ")
# family_2 = input("введите через запятую членов вашей семьи: ")
# if len(family_1.split(",")) > len(family_2.split(",")):
#     print(len(family_1.split(",")))
# elif len(family_2.split(",")) > len(family_1.split(",")):
#     print(len(family_2.split(",")))
# else:
#     print("Equal")

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# dictionary = {"title": "1+1",
#               "director": "Оливье Накаш и Эрик Толедано",
#               "year": "2011",
#               "budget": "€9 500 000",
#               "main_actor": "Франсуа Клюзе и Омар Си",
#               "slogan":"Sometimes you have to reach into someone else's world to find out what's missing in your own"
#               }
# for key, value in dictionary.items():
#     print(key)
#     print(value)
#     print(f"{key} {value}")

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum = 0
# for key, value in my_dictionary.items():
#     sum += value
# print(sum)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# list7 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list7))
# print(list(set(list7)))
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# list_yes = []
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# for i in set1:
#     for j in set2:
#         if i == j:
#             list_yes.append(i)
# print(list(set(list_yes)))
# print(set1 & set2)
# print(list(set((set1 - set2) | (set2 - set1))))
# print(set1.issubset(set2) or set2.issubset(set1))