from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

# Класс(модель) User, наследованный от BaseModel
class User(BaseModel):
    id: int
    username: str
    age: int

# get запрос по маршруту '/users', который возвращает словарь users.
@app.get("/users")
async def get_users() -> List[User]:
    return users

# post запрос по маршруту '/user/{username}/{age}'
#    Добавляет в список users объект User.
#    id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
#    Все остальные параметры объекта User - переданные в функцию username и age соответственно.
#    В конце возвращает созданного пользователя.
@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age",  example="24")]) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

#put запрос по маршруту '/user/{user_id}/{username}/{age}',
#    Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
#    В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example="1")],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age",  example="24")]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="The User was not found")

#delete запрос по маршруту '/user/{user_id}'
#    Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
#    В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID", example="1")]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="The User was not found")