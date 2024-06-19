from typing import Optional
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from . import schemas, crud


# It is advised to replace this secret - you can generate one by running `openssl rand -hex 32`
SECRET_KEY = "7f0691cb75a3ad5cd927ab7b5c1243a4014d06943f6098ac8a6eaba8aa3db901"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRATION_MINUTES = 30

context = CryptContext(schemes=["bcrypt"], deprecated="auto")
scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return context.verify(plain_password, hashed_password)

def get_password_hash(password:str) -> str:
    return context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# async def get_current_user(token: str = Depends(scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = schemas.TokenDataBase(username=username)
#     except JWTError:
#         raise credentials_exception
#     db_user = await crud.get_user(username=token_data.username)
#     if db_user is None:
#         raise credentials_exception

#     return db_user
