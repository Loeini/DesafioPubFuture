from sqlalchemy import create_engine, MetaData

senha = ''
engine = create_engine(f"mysql+pymysql://root{senha}@localhost:3306/desafiopubfuture")
meta = MetaData()
conexao = engine.connect()