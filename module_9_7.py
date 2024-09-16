'''Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three'''
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            if result % 2 == 0:
                return f"Составное\n{result}"
            else:
                return f'Простое\n{result}'
        else:
            return f"Число меньше или равное еденицы\n{result}"
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 3, 6)
print(result)