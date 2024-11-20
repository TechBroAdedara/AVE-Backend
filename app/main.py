
from datetime import datetime
import os
from typing import Annotated, Optional
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from icecream import ic
import logging

from sqlalchemy.exc import IntegrityError
from .routes import auth
from .routes.auth import (
    get_current_admin_user,
    get_current_student_user,
    get_current_user,
)
from .schemas.geofence import GeofenceCreate

from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.user import User
from app.models.geofence import Geofence
from app.models.attendanceRecord import AttendanceRecord
from .utils.algorithms import check_user_in_circular_geofence, generate_alphanumeric_code

if os.getenv("ENVIRONMENT") == "development":
    load_dotenv()


def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used
    finally:
        db.close()  # Close the session when done



# ----------------------------------------Allowed Origins--------------------------------------------
origins = [
    "http://localhost:3000",
    "http://localhost",
]
# ----------------------------------------FastAPI App Init--------------------------------------------
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Just for Development. Would be changed later.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)




# ----------------------------------------Routes--------------------------------------------
@app.get("/")
def index():
    return "Hello! Access our documentation by adding '/docs' to the url above"


# Webhook
# @app.webhooks.post("New attendance")
# def new_attendance():
#     return "Hello"




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
