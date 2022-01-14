from pydantic import BaseModel
import datetime


class Despesas(BaseModel):
    id: int
    id_conta: int
    valor: float
    data_pagamento: datetime.date
    data_pagamento_esperado: datetime.date
    tipo_despesa: str
