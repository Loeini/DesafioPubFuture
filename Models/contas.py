from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
import Config.database
from Config.database import meta

contas = Table(
    'contas', meta,
    Column('id', Integer, Primary_key=True),
    Column('usuario', String(255)),
    Column('saldo', Float),
    Column('tipo_conta', String(255)),
    Column('instituicao_financeira', String(255))
)

contas.create(Config.database.engine, checkfirst=True)
