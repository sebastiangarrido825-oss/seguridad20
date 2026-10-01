from fastapi import FastAPI, HTTPException, status
from random import choice

# 1. Initialize the FastAPI app instance
app = FastAPI()

personajes_anime = [
    "Goku",
    "Naruto Uzumaki",
    "Luffy",
    "Levi Ackerman",
    "Light Yagami",
    "Satoru Gojo",
    "Tanjiro Kamado",
    "Izuku Midoriya",
    "Vegeta",
    "Edward Elric",
    "Kakashi Hatake",
    "Killua Zoldyck",
    "Ichigo Kurosaki",
    "Eren Yeager",
    "Mikasa Ackerman",
    "Roronoa Zoro",
    "Nezuko Kamado",
    "Saitama",
    "Rem",
    "Kurumi Tokisaki"
]

# 2. Define the path and HTTP method using a decorator
@app.get("/")
def read_root():
    # 3. Return a dictionary (FastAPI automatically converts this to JSON)
    return {"message": "Hello World!!!!"}

@app.get("/api/personajes/")
def personajes(limit: int = 5):
    return {
        "personajes": personajes_anime[:limit]
    }

@app.get("/api/personajes/{id}")
def un_personajes(id: int):
    if id <= len(personajes_anime) - 1:
        return {
            "personajes": personajes_anime[id]
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong on our end."
        )
