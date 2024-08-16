'''Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует.
 В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"

Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

Вывод в консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует urban_pythonist'''
import hashlib
import time
from pynput import keyboard

'''Класс пльзователя, содержащий: никнэйм, пароль и возраст'''
class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    '''Обращение usera к самому себе'''
    def desc(self):
        print(self.nickname, self.password, self.age)

'''Класс видео, содержащий: название, продолжительность, время остановки и оганичение по возрасту'''
class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

'''Класс УрТубэ содержит: список объектов User, список объектов Video, текущий пользователь, User'''
class UrTube:
    current_user = None

    def __init__(self):
        self.users = []
        self.videos = []
        self.playing = False

    '''Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.'''
    def log_in(self, login, password):
        hashed_pasword = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == login and user.password == hashed_pasword:
                self.current_user = user
                print(f'Вы вошли{user.nicname}')
                return
            else:
                print('Данные не найдены или не верны!')
                return
    '''Добовление нового пользователя'''
    def add_user(self, *new_user):
        for user in new_user:
            self.users.append(user)

    '''Выполняем desc для пользователей'''
    def discribe(self):
        for user in self.users:
            print(user.desc)

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует!')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.playing = not self.playing

    def watch_video(self, title):
        for video in self.videos:
            if self.current_user == None:
                print('Войдите в аккаунт, чтобы смотреть видео')
                return
            elif video.title == title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страцу')
                    return

                self.playing = True
                listner = keyboard.Listener(on_press=self.on_press)
                listner.start()

                while video.time_now < video.duration:
                    if self.playing:
                        print(f'Просмотр видео "{title}": {video.time_now} секунд')
                        time.sleep(1)
                        video.time_now += 1
                    else:
                        print('Пауза. Нажмите "пробел" для возобновления')
                        time.sleep(1)
                print('Конец видео')
                video.time_now = 0
                listner.stop()
                return
        print('Попытка воспроизведения несуществующего видео')
        return


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')