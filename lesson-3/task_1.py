"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


import time

def time_it(func):
    def wrapper(*args):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrapper

@time_it
def list(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj


@time_it
def dict(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_obj


list(10000)
dict(10000)