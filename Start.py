from fastapi import FastAPI
from Routes.index import conta, receita, despesa

app = FastAPI()


app.include_router(conta,
    prefix="/conta",
    tags=["conta"]
)
app.include_router(receita,
    prefix="/receita",
    tags=["receita"]
)
app.include_router(despesa,
    prefix="/despesa",
    tags=["despesa"]
)
