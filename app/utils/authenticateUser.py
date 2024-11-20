from passlib.context import CryptContext
from app.models import User
from sqlalchemy import or_
from fastapi import HTTPException, status, Security
from fastapi.security import APIKeyHeader, APIKeyQuery
import os
from dotenv import load_dotenv

if os.getenv("ENVIRONMENT") == "development":
    load_dotenv()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(user_pass, password: str, db):
    user = (
        db.query(User)
        .filter(or_(User.email == user_pass, User.user_matric == user_pass))
        .first()
    )

    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


API_KEYS = os.getenv("API_KEYS").split(",")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def get_api_key(
    api_key_header: str = Security(api_key_header),
) -> str:
    """Retrieve and validate an API key from the query parameters or HTTP header.

    Args:
        api_key_query: The API key passed as a query parameter.
        api_key_header: The API key passed in the HTTP header.

    Returns:
        The validated API key.

    Raises:
        HTTPException: If the API key is invalid or missing.
    """
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
