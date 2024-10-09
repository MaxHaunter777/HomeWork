'''Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях,
которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.'''
import multiprocessing as mp
import requests
from PIL import Image
import queue
from queue import Empty
import os
import sys

# За счёт библиотеки requests делаем запросы на сайт и скачиваем фотографии
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/89.0.4389.72 Safari/537.36'}
session = requests.Session()
session.headers.update(user_agent)

class Download:
    def pics_downloader(num_of_pics):
        for num in range(num_of_pics):
            response = session.get('https://picsum.photos/200', allow_redirects=True, stream=True)
            with open(f'./{num}.jpg', 'wb') as picture:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        picture.write(chunk)
            print(f'Скачано {num + 1} фото из {num_of_pics}')

# За счёт библиотеки pillow, меняем размер, цвет фотографий и формат с jpg на png
class Change():

    def resize_image(image_path, queue):
        for image_path in image_path:
            image = Image.open(image_path)
            image = image.resize((800, 600))
            queue.put((image_path, image))

    def change_color_format(queue):
        while True:
            try:
                image_path, image = queue.get(timeout= 5)
            except Empty:
                break
            image = image.convert('L')
            image.save(image_path)
            jpg_images = [image for image in os.listdir() if image.endswith('.jpg')]
            for jpg_image in jpg_images:
                try:
                    new_name = jpg_image.split('.')[0] + '.png'
                    Image.open(jpg_image).save(f'./image2/{new_name}')
                except IOError as error:
                    print('Couldn\'t read {} '.format(jpg_image))

if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    Download.pics_downloader(20)

    for image in range(0, 20):
        data.append(f'./{image}.jpg')

    resize_process = mp.Process(target=Change.resize_image, args=(data, queue))
    change_process = mp.Process(target=Change.change_color_format, args=(queue, ))

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()

    print('Фотогрфии изменены')