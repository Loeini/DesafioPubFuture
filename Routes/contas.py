from fastapi import APIRouter
from Config.database import conexao
from Models.index import contas, despesas, receitas
from Schemas.index import Contas
import datetime


conta = APIRouter()


@conta.get("/")  # Busca sem filtro, busca todas as contas.
async def read_all_account():
    return conexao.execute(contas.select()).fetchall()


@conta.get("/:{id}")  # Busca com filtro de id.
async def read_account_by_id(id: int):
    return conexao.execute(contas.select().where(contas.c.id == id)).fetchall()


@conta.get("/:{id}")  # Busca do saldo pela id da conta.
async def read_balance_by_id(id: int):  # esse saldo é valido?
    return conexao.execute(contas.select(contas.saldo).where(contas.c.id == id)).fetchall()


@conta.post("/")  # Cadastro de novas contas.
async def write_account(conta: Contas):
    conexao.execute(contas.insert().values(
        usuario=conta.usuario,
        tipo_conta=conta.tipo_conta,
        saldo=0,
        instituicao_financeira=conta.instituicao_financeira
    ))
    return conexao.execute(contas.select()).fetchall()


@conta.put("/{id}")  # Atualização de conta.
async def update_account(id: int):
    conexao.execute((contas.update(
        usuario=conta.usuario,
        tipo_conta=conta.tipo_conta,
        instituicao_financeira=conta.instituicao_financeira
    ).where(contas.c.id == id)))


@conta.delete("/{id}")  # Remover conta.
async def delete_account(id: int):
    conexao.execute(contas.delete().where(contas.c.id == id))
    return conexao.execute(contas.select()).fetchall()


@conta.put("/")  # Transferir saldo entre contas
async def transfer_data(id_origem: int, id_destino: int, valor_transferencia: float):
    conexao.execute(despesas.insert().values(
        id_conta=id_origem,
        valor=valor_transferencia,
        data_pagamento=datetime.date.today(),
        tipo_despesa='Transferencia.'
    ))
    conexao.execute(receitas.insert().values(
        id_conta=id_destino,
        valor=valor_transferencia,
        data_recebimento=datetime.date.today(),
        tipo_receita='Transferencia.',
        descricao='Transferencia.'
    ))
    conexao.execute(contas.update().values(saldo=contas.c.saldo - valor_transferencia).where(contas.c.id == id_origem))
    conexao.execute(contas.update().values(saldo=contas.c.saldo + valor_transferencia).where(contas.c.id == id_destino))
    return conexao.execute(contas.select()).fetchall()

