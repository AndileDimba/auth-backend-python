from fastapi import FastAPI
from app.api.endpoints import auth, user
from app.infrastructure.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def health_check():
    return {"status": "ok"}