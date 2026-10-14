from fastapi import FastAPI, HTTPException
from rental import get_bicycles, rent_bicycle, return_bicycle, get_rentals
from fastapi.middleware.cors import CORSMiddleware
from rental import (
    get_bicycles,
    rent_bicycle,
    return_bicycle,
    get_rentals,
    get_users
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/bicycles")
def get_bicycles_api():
    return get_bicycles()


@app.post("/bicycles/{bicycle_id}/rent")
def rent_bicycle_api(bicycle_id: int, user_id: int):
    result = rent_bicycle(bicycle_id, user_id)

    if result == "not_found":
        raise HTTPException(
            status_code=404,
            detail="Велосипеда нет"
        )

    if result == "unavailable":
        raise HTTPException(
            status_code=409,
            detail="Велосипед недоступен"
        )

    if result == "user_not_found":
        raise HTTPException(
            status_code=404,
            detail="Пользователь не найден"
        )

    return {"message": "Велосипед успешно арендован"}

@app.post("/bicycles/{bicycle_id}/return")
def return_bicycle_api(bicycle_id: int):
    result = return_bicycle(bicycle_id)

    if result == "not_found":
        raise HTTPException(
            status_code=404,
            detail="Велосипеда нет"
        )

    if result == "not_rented":
        raise HTTPException(
            status_code=409,
            detail="Велосипед не находится в аренде"
        )

    return {"message": "Велосипед успешно возвращён"}

@app.get("/rentals")
def get_rentals_api():
    return get_rentals()

@app.get("/users")
def get_users_api():
    return get_users()

@app.get("/")
def home():
    return FileResponse("index.html")