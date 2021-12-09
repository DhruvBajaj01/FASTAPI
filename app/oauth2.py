from jose import JWTError, jwt
from datetime import datetime, timedelta

#secret_key 
#Algorithm
#expiration time


SECRET_KEY = "ky2M2hhRasfTcv2HH946nxuR4WakN6tgdZXkcHzsL2TVtWhN96"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def Create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() +timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt