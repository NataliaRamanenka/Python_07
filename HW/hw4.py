import functools
import time
from my_calc import my_calc
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
def square(a):
    return (4*a, a*a, round((a*a + a*a) ** 0.5, 2))
# print(square(2))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def person(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# (person(name="Jane"))
# (person(name="John", last_name="Smith", age=35, position="web developer"))
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x >= 0, my_list))
# print(new_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# print(functools.reduce(lambda a, b: a * b, new_list))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# def time_work(func):
#     def inner(*arg):
#         start = time.time()
#         func(*arg)
#         end = time.time() - start
#         print(f"Время выполнения фунции: {end}")
#     return inner
#
# @time_work
# def square(a):
#     return (4*a, a*a, round((a*a + a*a) ** 0.5, 2))
#
# square(2)

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
# print(my_calc(6,0,"/"))
# print(my_calc(6,10,"/"))