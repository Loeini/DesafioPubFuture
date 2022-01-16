Passo a passo:

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

Métodos:

na tabela contas:
    read_all_account --> Busca sem filtro, busca todas as contas;
    read_account_by_id --> Busca com filtro de id.
    read_balance_by_id --> Busca do saldo pelo id da conta.
    write_account --> Cadastro de novas contas.
    update_account --> Atualização de conta.
    delete_account --> Remover conta.
    transfer_data --> Transferir saldo entre contas.

na tabela receitas:
    read_all_income --> Busca sem filtro, busca todas as receitas.
    read_income_by_account_id --> Busca com filtro de conta.
    read_income_by_account_id_date --> Busca com filtro de periodo.
    read_income_by_type --> Busca por tipo de receita.
    write_income --> Cadastro de novas despesas.
    update_income --> Edição de receita.
    delete_income --> Remover receita.

na tabela despesas:
    read_all_expense --> Busca sem filtro, busca todas as despesa.
    read_expense_by_account_id --> Busca com filtro de conta.
    read_expense_by_account_id_date --> Busca com filtro de periodo e conta.
    read_expense_by_type --> Busca por tipo de despesa.
    write_expense --> Cadastro de novas despesas.
    update_expense --> Edição de despesa.
    delete_expense --> Remover despesa.
