'''Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта,
 чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}'''
import inspect
import sys
def introspection_info(obj):
    attr = [atr_name  for atr_name in dir(obj)
                 if not callable(getattr(obj, atr_name))]
    object_methods = [method_name for method_name in dir(obj)
                      if callable(getattr(obj, method_name))]
    return (f'Тип объекта: {type(obj)}'
            f'\nАтрибуты объекта: {attr}'
            f'\nМетоды объекта: {object_methods}'
            f'\nМодуль, к которому объект принадлежит: {getattr(obj, '__module__', __name__)}')



number_info = introspection_info(42)
print(number_info)

