from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

#Создайте словарь
users = {'1': 'Имя: Example, возраст: 18'}

# get запрос по маршруту '/users', который возвращает словарь users.
@app.get("/users")
async def get_users() -> dict:
    return users

# post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки
# "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age",  example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

#put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку
# "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example="1")],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username, example="UrbanUser"")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age",  example="24")]) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

#delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example="1")]) -> str:
    users.pop(str(user_id))
    return f"The user {user_id} has been deleted"
