from fastapi import FastAPI
from Routes.index import conta, receita, despesa

app = FastAPI()


app.include_router(conta)  # Criar mais? Ou manter no mesmo.
#app.include_router(receita)
#app.include_router(despesa)
