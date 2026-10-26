from fastapi import FastAPI
from dependencies import bcrypt_context

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# para rodar o codigo, executar no terminal: uvicorn main:app --reload

# endpoint:
# hashtagtreinamentos.com/ordens

# Rest APIS:
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar