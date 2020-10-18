def my_func(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        res = n1 / n2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return "Нельзя делить на ноль"

    return res


n1 = input("Введите первое число:")
n2 = input("Введите второе число:")

print(f'Результат:  {my_func(n1, n2)}')

