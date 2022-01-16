from fastapi import APIRouter
from Config.database import conexao
from Models.index import receitas
from Schemas.index import Receitas
from Models.index import contas
from Schemas.index import Contas
import datetime

receita = APIRouter()


@receita.get("/")  # Busca sem filtro, busca todas as receitas.
async def read_all_income():
    return conexao.execute(receitas.select()).fetchall()


@receita.get("/:{id_conta}")  # Busca com filtro de conta.
async def read_income_by_account_id(id_conta: int):
    return conexao.execute(receitas.select().where(receitas.c.id_conta == id_conta)).fetchall()


@receita.get("/")  # Busca com filtro de periodo.
async def read_income_by_account_id_date(id_conta: int, data_inicial: datetime.date, data_final: datetime.date):
    return conexao.execute(
        receitas.select().where(receitas.c.id_conta == id_conta, receitas.c.data_pagamento >= data_inicial,
                                receitas.c.data_pagamento <= data_final)).fetchall()


@receita.get("/:{tipo_receita}")  # Busca por tipo de receita.
async def read_income_by_type(tipo_receita: str):
    return conexao.execute(receitas.select().where(receitas.c.tipo_receita == tipo_receita)).fetchall()


@receita.post("/")  # Cadastro de novas despesas.
async def write_income(receita: Receitas):
    conexao.execute(receitas.insert().values(
        id_conta=receita.id_conta,
        valor=receita.valor,
        data_recebimento=receita.data_recebimento,
        data_recebimento_esperado=receita.data_recebimento_esperado,
        tipo_receita=receita.tipo_receita,
        descricao=receita.descricao
    ))
    conexao.execute(contas.update().values(saldo = (contas.c.saldo + receita.valor)).where(contas.c.id == receita.id_conta))
    return conexao.execute(receitas.select().where(receitas.c.id_conta == receita.id_conta)).fetchall()


@receita.put("/{id}")  # Edição de receita.
async def update_income(id: int, receita:Receitas):
    valor_anterior = conexao.execute(receitas.select(receitas.valor).where(receitas.c.id == id))
    conexao.execute((receitas.update(
        valor=receita.valor,
        data_recebimento=receita.data_recebimento,
        data_recebimento_esperado=receita.data_recebimento_esperado,
        tipo_receita=receita.tipo_receita,
        descricao=receita.descricao
    ).where(receitas.c.id == id)))
    saldo_atual = conexao.execute(contas.select(contas.saldo).where(contas.c.id == receita.id_conta))
    diferenca = valor_anterior - receita.valor
    conexao.execute(contas.update(saldo=saldo_atual - diferenca).where(contas.c.id == receita.id_conta))
    return conexao.execute(receitas.select().where(receitas.c.id_conta == receita.id_conta)).fetchall()


@receita.delete("/{id}")  # Remover receita.
async def delete_income(id: int):
    id_conta = conexao.execute(receitas.select(receitas.id_conta).where(receitas.c.id == id))
    valor_receita = conexao.execute(receitas.select(receitas.valor).where(receitas.c.id == id))
    saldo_atual = conexao.execute(contas.select(contas.saldo).where(contas.c.id == id_conta))
    conexao.execute(receitas.delete().where(receitas.c.id == id))
    conexao.execute(contas.update(saldo=saldo_atual - valor_receita).where(contas.c.id == id_conta))
    return conexao.execute(receitas.select()).fetchall()
