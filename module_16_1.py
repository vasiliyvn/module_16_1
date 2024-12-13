from fastapi import FastAPI
from typing import Optional


app = FastAPI()
#python -m uvicorn main:app
@app.get('/')
async def marshrut() :
    return f'Главная страница'
@app.get('/user/admin')
async def marshrut() :
    return f'Вы вошли как администратор'
@app.get('/user/{user_id}')
async def marshrut(user_id: str) :
    return f'Вы вошли как пользователь № {user_id}'
@app.get('/user')
async def marshrut(username: str, age: int) :
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
