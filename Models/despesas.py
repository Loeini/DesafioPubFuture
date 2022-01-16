from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float
import Config.database
from Config.database import meta

despesas = Table(
    'despesas', meta,
    Column('id', Integer, autoincrement=True, primary_key=True, nullable=False),
    Column('id_conta', Integer),
    Column('valor', Float),
    Column('data_pagamento', Date),
    Column('data_pagamento_esperado', Date),
    Column('tipo_despesa', String(255))
)

despesas.create(Config.database.engine, checkfirst=True)
