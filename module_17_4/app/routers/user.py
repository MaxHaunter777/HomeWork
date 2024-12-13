# В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user',
# а также следующие маршруты, с пустыми функциями:
#    get '/' с функцией all_users.
#    get '/user_id' с функцией user_by_id.
#    post '/create' с функцией create_user.
#    put '/update' с функцией update_user.
#    delete '/delete' с функцией delete_user.

from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated

from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete

# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=['user'])

@router.get('/')
# Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


# Для извлечения записи используйте ранее импортированную функцию select.
#    Дополнительно принимает user_id.
#    Выбирает одного пользователя из БД.
#    Если пользователь не None, то возвращает его.
#    В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.get("/user/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail=f"User this id={user_id} was not found")
    return user

@router.post('/create')
# Для добавления используйте ранее импортированную функцию insert.
#    Дополнительно принимает модель CreateUser.
#    Подставляет в таблицу User запись значениями указанными в CreateUser.
#    В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
#    Обработку исключения существующего пользователя по user_id или username можете сделать по желанию
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    slug = slugify(create_user.username) or "default-slug"
    new_user = User(
        username=create_user.username,
        firstname=create_user.firstname,
        lastname=create_user.lastname,
        age=create_user.age,
        slug=slug
    )
    db.execute(insert(User).values(username=new_user.username,
                                       firstname=new_user.firstname,
                                       lastname=new_user.lastname,
                                       age=new_user.age,
                                       slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'User create successful'}

@router.put('/update/{id}')
# Для обновления используйте ранее импортированную функцию update.
#    Дополнительно принимает модель UpdateUser и user_id.
#    Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser.
#    Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
#    В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    existing_user = db.scalars(select(User).where(User.id == user_id)).first()
    if existing_user:
        db.execute(update(User).where(User.id == user_id).values(
                                        firstname=update_user.firstname,
                                        lastname=update_user.lastname,
                                        age=update_user.age
                                        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User update is successful'}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User this id={user_id} not found'
        )

@router.delete('/delete/{user_id}')
# Для удаления используйте ранее импортированную функцию delete.
#    Всё должно работать аналогично функции update_user, только объект удаляется.
#    Исключение выбрасывать то же.
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user:
        db.execute(delete(User).where(User.id == user_id))
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "User delete is successful!"}
    else:
        raise HTTPException(status_code=404, detail="Usert his id={user_id} was not found")