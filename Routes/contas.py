from fastapi import APIRouter
from Config.database import conexao
from Models.index import contas
from Schemas.index import Contas

conta = APIRouter()


@conta.get("/")  # Busca sem filtro, busca todas as contas.
async def read_data():
    return conexao.execute(contas.select()).fetchall()


@conta.get("/:{id}")  # Busca com filtro de id.
async def read_data(id: int):
    return conexao.execute(contas.select().where(contas.c.id == id)).fetchall()


@conta.get("/:{saldo}")  # Busca do saldo pela id da conta.
async def read_data(saldo: float):
    return conexao.execute(contas.select().where(contas.c.id == id)).fetchall()


@conta.post("/")  # Cadastro de novas contas.
async def write_data(conta: Contas):
    conexao.execute(contas.insert().values(
        usuario=conta.usuario,
        tipo_conta=conta.tipo_conta,
        instituicao_financeira=conta.instituicao_financeira
    ))
    return conexao.execute(contas.select()).fetchall()


@conta.put("/{id}")  # Atualização de conta.
async def update_data(id: int):
    conexao.execute((contas.update(
        usuario=conta.usuario,
        tipo_conta=conta.tipo_conta,
        instituicao_financeira=conta.instituicao_financeira
    ).where(contas.c.id == id)))


@conta.delete("/{id}")  # Remover conta.
async def delete_data(id: int):
    conexao.execute(contas.delete().where(contas.c.id == id))
    return conexao.execute(contas.select()).fetchall()


@conta.put("/")  # Transferir saldo entre contas
async def transfer_data()  #???






