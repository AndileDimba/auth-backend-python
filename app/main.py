from fastapi import FastAPI
from sqlalchemy import text
from app.api.endpoints import auth, user
from app.infrastructure.database import Base, engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)
logger.info("Database tables created")

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        logger.info(f"Pre-start connection test successful: {result.scalar()}")
except Exception as e:
    logger.error(f"Pre-start connection failed: {e}")
    # Exit application if connection fails
    raise SystemExit("Database connection failed. Application cannot start.")

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def health_check():
    return {"status": "ok"}