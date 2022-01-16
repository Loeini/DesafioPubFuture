from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float
import Config.database
from Config.database import meta

receitas = Table(
    'receitas', meta,
    Column('id', Integer, primary_key=True),
    Column('id_conta', Integer),
    Column('valor', Float),
    Column('data_recebimento', Date),
    Column('data_recebimento_esperado', Date),
    Column('tipo_receita', String(255)),
    Column('descricao', String(255))
)

receitas.create(Config.database.engine, checkfirst=True)
