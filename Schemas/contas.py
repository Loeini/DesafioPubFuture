from pydantic import BaseModel


class Contas(BaseModel):
    id: int
    usuario: str
    saldo: float
    tipo_conta: str
    instituicao_financeira: str
