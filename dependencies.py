from fastapi import Depends, HTTPException
from models import db
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from passlib.context import CryptContext
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

load_dotenv()

SecretKey = os.getenv("SecretKey")
Algorithm = os.getenv("Algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl = "auth/login_form")

def pegar_sessao():
    try:
        Session = sessionmaker(bind= db)
        session = Session()
        yield session
    finally:
        session.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SecretKey, Algorithm)
        id_usuario = int(dic_info.get("sub"))

        #dic_info["sub"] é um segundo modelo, porém o .get é melhor pois não me entrega nenhum erro!!

    except JWTError as erro:
        print(erro)
        raise HTTPException(status_code = 401, detail = "Acesso Negado, Verifique a validade do token!")
    #verificar se o token é válido
    #extrair o ID do usuário do token 
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code = 401, detail = "Acesso Inválido")
    return usuario