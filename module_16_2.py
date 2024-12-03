from fastapi import FastAPI, Path
from typing import Annotated

# Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
app = FastAPI()

# Создайте маршрут к главной странице - "/"
# По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def root():
    return {"message": "Главная страница"}

# Создайте маршрут к странице администратора - "/user/admin"
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

# Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
#    Должно быть целым числом
#    Ограничено по значению: больше или равно 1 и меньше либо равно 100.
#    Описание - 'Enter User ID'
@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example="1")]):
    return {f"Вы вошли как пользователь №{user_id}"}

# Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
#   username - строка, age - целое число.
#   username ограничение по длине: больше или равно 5 и меньше либо равно 20.
#   age ограничение по значению: больше или равно 18 и меньше либо равно 120.
#   Описания для username и age - 'Enter username' и 'Enter age' соответственно.
@app.get("/user/{username}/{age}")
async def get_user(
        username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
