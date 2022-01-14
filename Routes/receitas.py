from fastapi import APIRouter
from Config.database import conexao
from Models.index import receitas
from Schemas.index import Receitas
from Models.contas import contas

receita = APIRouter()


@receita.get("/")  # Busca sem filtro, busca todas as receitas. OK
async def read_data():
    return conexao.execute(receitas.select()).fetchall()


@receita.get("/:{id_conta}")  # Busca com filtro de periodo.
async def read_data(valor: float, tipo_receita: str):
    return conexao.execute(receitas.select().where(contas.c.id == id)).fetchall() #como filtrar período


@receita.get("/:{tipo_despesa}")  # Busca por tipo de receita.
async def read_data(valor: float):
    return conexao.execute(receitas.select().where(receitas.c.tipo_receita == tipo_receita)).fetchall()


@receita.post("/")  # Cadastro de novas despesas.
async def write_data(receita: Receitas):
    conexao.execute(receitas.insert().values(
        id_conta=receita.id_conta,
        valor=receita.valor,
        data_recebimento=receita.data_recebimento,
        data_recebimento_esperado=receita.data_recebimento_esperado,
        tipo_receita=receita.tipo_receita,
        descricao=receita.descricao
    ))
    return conexao.execute(receitas.select().where(receitas.c.id_conta == id_conta)).fetchall()


@receita.put("/{id}")  # Edição de receita.
async def update_data(id: int):
    conexao.execute((receitas.update(
        valor=receita.valor,
        data_recebimento=receita.data_recebimento,
        data_recebimento_esperado=receita.data_recebimento_esperado,
        tipo_receita=receita.tipo_receita,
        descricao=receita.descricao
    ).where(receitas.c.id == id)))


@receita.delete("/{id}")  # Remover receita. OK
async def delete_data(id: int):
    conexao.execute(receitas.delete().where(receitas.c.id == id))
    return conexao.execute(receitas.select()).fetchall()
