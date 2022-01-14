from pydantic import BaseModel
import datetime


class Receitas(BaseModel):
    id: int
    id_conta: int
    valor: float
    data_recebimento: datetime.date
    data_recebimento_esperado: datetime.date
    tipo_receita: str
    descricao: str
