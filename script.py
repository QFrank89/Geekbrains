list = [1, 2, 3, 4, 5]
list_1 = []
for el in list:
    list_1.append(el * 2)
print(list_1)


my_dict = {'Имя:' 'Сергей', 'Возраст:' '31', 'Страна:' 'Россия'}
for key, value in my_dict.items():
    print(f"{key} - {value}")