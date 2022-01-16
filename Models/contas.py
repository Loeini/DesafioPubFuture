from sqlalchemy import Table, Column, Identity
from sqlalchemy.sql.sqltypes import Integer, String, Float
import Config.database
from Config.database import meta

contas = Table(
    'contas', meta,
    Column('id', Integer, autoincrement=True, primary_key=True, nullable=False),
    Column('usuario', String(255)),
    Column('saldo', Float, nullable=False),
    Column('tipo_conta', String(255)),
    Column('instituicao_financeira', String(255))
)

contas.create(Config.database.engine, checkfirst=True)

