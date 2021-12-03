from fastapi import APIRouter, Depends, status,HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from app import models
from .. import database, schemas,utils

router = APIRouter(
    tags  = ['Authentication']
)

@router.post('/login')
def login(user_cred: schemas.UserLogin,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Inavlid Credentials")

    if not utils.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")
    
    return {"token ":"successfull"}