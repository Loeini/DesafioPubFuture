from pydantic import BaseModel


class Receitas(BaseModel):
    id: int
    id_conta: int
    valor: float
    data_recebimento: #data
    data_recebimento_esperado:
    tipo_receita: str