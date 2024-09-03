'''Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:
Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
Пример возможного вывода:
Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.'''

import datetime
import os


time = datetime.datetime.now()
directory = r'C:\pythonProject\newProject1'


for root, dirs, files in os.walk(directory):
  for file in files:
    import os.path
    filepath = os.path.join('С', 'pythonProject', 'newProject1', 'module_7_5.py')
    filetime = os.path.getmtime(r'C:\pythonProject\newProject1\module_7_5.py')
    import time
    time.ctime(filetime)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(r'C:\pythonProject\newProject1\module_7_5.py')
    parent_dir = os.path.isdir(r'C:\pythonProject\newProject1')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')