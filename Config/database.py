from sqlalchemy import create_engine, MetaData

engine = create_engine(f"mysql+pymysql://root@localhost:3306/desafiopubfuture")
meta = MetaData()
conexao = engine.connect()