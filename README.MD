# Desafio Pub Future

## Passo a passo:

1 - É necessário ter o MySql instalado, e criar o database desafiopubfuture no Mysql;

2 - Em um terminal, escrever os seguintes códigos (rodar um por um):
    pip install virtualenv
    virtualenv venv
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned  (este deve rodar do app PowerShell do Windows)
    venv/Scripts/activate 
    pip install fastapi sqlalchemy pymysql uvicorn
    uvicorn Start:app --reload

3 - Acessar a API REST: http://localhost:8000/docs#/

4 - Adequar a string de conexão do Mysql (em database.py) para o usuário e senha (caso necessário) do teste.

## Métodos:

na tabela contas:
- read_all_account --> Busca sem filtro, busca todas as contas
  - parâmetros: sem parâmetros;
######
- read_account_by_id --> Busca com filtro de id
  - parâmetros: **id** (id da conta);
######
- read_balance_by_id --> Busca do saldo pelo id da conta
  - parâmetros: **id** (id da conta);
######
- write_account --> Cadastro de novas contas
  - parâmetros: sem parâmetros (mas os campos do json podem ser preenchidos para testes);
######
- update_account --> Atualização de conta
  - parâmetros: **id** (id da conta);
######
- delete_account --> Remover conta
  - parâmetros: **id** (id da conta);
######
- transfer_data --> Transferir saldo entre contas
  - parâmetros: **id_origem** (id da conta que sairá algum valor), **id_destino** (id da conta que receberá algum valor), **valor_transferencia** (valor a ser transferido);
######

na tabela receitas:
- read_all_income --> Busca sem filtro, busca todas as receitas
  - parâmetros: sem parâmetros;
######
- read_income_by_account_id --> Busca com filtro de conta
  - parâmetros: **id_conta** (mesmo id da ta tabela conta);
######
- read_income_by_account_id_date --> Busca com filtro de periodo
  - parâmetros: *id_conta** (mesmo id da ta tabela conta), **data_inicial** (data no formato yyyy-mm-dd), **data_final** (data no formato yyyy-mm-dd);
######
- read_income_by_type --> Busca por tipo de receita
  - parâmetros: **tipo_receita** (string cadastrada como um tipo de receita)
######
- write_income --> Cadastro de novas despesas
  - parâmetros: sem parâmetros (mas os campos do json podem ser preenchidos para testes);
######
- update_income --> Edição de receita
  - parâmetros: **id** (id da receita cadastrada);
######
- delete_income --> Remover receita
  - parâmetros: **id** (id da receita cadastrada);
######

na tabela despesas:
- read_all_expense --> Busca sem filtro, busca todas as despesa
  - parâmetros: sem parâmetros;
######
- read_expense_by_account_id --> Busca com filtro de conta
  - parâmetros: *id_conta** (mesmo id da ta tabela conta);
######
- read_expense_by_account_id_date --> Busca com filtro de periodo e conta
  - parâmetros: *id_conta** (mesmo id da ta tabela conta), **data_inicial** (data no formato yyyy-mm-dd), **data_final** (data no formato yyyy-mm-dd);
######
- read_expense_by_type --> Busca por tipo de despesa 
  - parâmetros: **tipo_receita** (string cadastrada como um tipo de receita);
######
- write_expense --> Cadastro de novas despesas
  - parâmetros: sem parâmetros (mas os campos do json podem ser preenchidos para testes);
######
- update_expense --> Edição de despesa
  - parâmetros: **id** (id da despesa cadastrada);
######
- delete_expense --> Remover despesa
  - parâmetros: **id** (id da despesa cadastrada);
######
