from fastapi import APIRouter
from Config.database import conexao
from Models.index import despesas
from Schemas.index import Despesas
from Models.index import contas
import datetime

despesa = APIRouter()


@despesa.get("/")  # Busca sem filtro, busca todas as despesa. OK
async def read_all_expense():
    return conexao.execute(despesas.select()).fetchall()


@despesa.get("/:{id_conta}")  # Busca com filtro de conta. OK
async def read_expense_by_account_id(id_conta: int):
    return conexao.execute(despesas.select().where(despesas.c.id_conta == id_conta)).fetchall()


@despesa.get("/")  # Busca com filtro de periodo e conta.
async def read_expense_by_account_id_date(id_conta: int, data_inicial: datetime.date, data_final: datetime.date):
    return conexao.execute(
        despesas.select().where(despesas.c.id_conta == id_conta, despesas.c.data_pagamento >= data_inicial,
                                despesas.c.data_pagamento <= data_final)).fetchall()  # como filtrar período


@despesa.get("/:{tipo_despesa}")  # Busca por tipo de despesa.
async def read_expense_by_type(tipo_despesa: str):
    return conexao.execute(despesas.select().where(despesas.c.tipo_despesa == tipo_despesa)).fetchall()


@despesa.post("/")  # Cadastro de novas despesas.
async def write_expense(despesa: Despesas):
    conexao.execute(despesas.insert().values(
        id_conta=despesa.id_conta,
        valor=despesa.valor,
        data_pagamento=despesa.data_pagamento,
        data_pagamento_esperado=despesa.data_pagamento_esperado,
        tipo_despesa=despesa.tipo_despesa
    ))
    saldo_atual = conexao.execute(contas.select(contas.saldo).where(contas.c.id == despesa.id_conta))
    conexao.execute(contas.update(saldo=saldo_atual - despesa.valor).where(contas.c.id == despesa.id_conta))
    return conexao.execute(despesas.select().where(despesas.c.id_conta == despesa.id_conta)).fetchall()


@despesa.put("/{id}")  # Edição de despesa.
async def update_expense(id: int):
    valor_anterior = conexao.execute(despesas.select(despesas.valor).where(despesas.c.id == id))
    conexao.execute((despesas.update(
        valor=despesa.valor,
        data_pagamento=despesa.data_pagamento,
        data_pagamento_esperado=despesa.data_pagamento_esperado,
        tipo_despesa=despesa.tipo_despesa
    ).where(despesas.c.id == id)))
    saldo_atual = conexao.execute(contas.select(contas.saldo).where(contas.c.id == despesa.id_conta))
    diferenca = valor_anterior - despesa.valor
    conexao.execute(contas.update(saldo=saldo_atual + diferenca).where(contas.c.id == despesa.id_conta))
    return conexao.execute(despesas.select().where(despesas.c.id_conta == despesa.id_conta)).fetchall()


@despesa.delete("/{id}")  # Remover despesa.
async def delete_expense(id: int):
    id_conta = conexao.execute(despesas.select(despesas.id_conta).where(despesas.c.id == id))
    valor_despesa = conexao.execute(despesas.select(despesas.valor).where(despesas.c.id == id))
    saldo_atual = conexao.execute(contas.select(contas.saldo).where(contas.c.id == id_conta))
    conexao.execute(despesas.delete().where(despesas.c.id == id))
    conexao.execute(contas.update(saldo=saldo_atual + valor_despesa).where(contas.c.id == id_conta))
    return conexao.execute(despesas.select()).fetchall()
