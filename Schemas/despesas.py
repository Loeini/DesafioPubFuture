from pydantic import BaseModel


class Despesas(BaseModel):
    id: int
    id_conta: int
    valor: float
    data_pagamento: #data
    data_pagamento_esperado:
    tipo_despesa: str
