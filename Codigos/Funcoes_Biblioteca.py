import pandas as pd
import pyodbc

LOGIN = 'admin'
SENHA = 'Exp2025$'

#=== 1º Passo - Função para buscar a tabela desejada no server expertise_01 ===#
def buscar_livros(Server, Database, 
                #   Usuario, Senha, 
                  banco):
    # Conexão para criar o banco de dados 
    dados_conexao = (
    "DRIVER=ODBC Driver 17 for SQL Server;"   # "Driver={SQL Server};"  / "DRIVER=ODBC Driver 17 for SQL Server;"
    "Server="+Server+";"
    "Database="+Database+";"
    # "UID="+Usuario+";"
    # "PWD="+Senha+";"
    "Trusted_Connection=yes;"  # "Encrypt=yes;TrustServerCertificate=yes"  /  "Trusted_Connection=yes;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

    comando_sql = f"""SELECT * FROM {banco}"""

    dados = pd.read_sql(comando_sql, conexao)

    conexao.close()
    return dados


#=== 2º Passo - Alterar os status dos livros (Disponível, Emprestado, Não encontrado) ===#
def alterar_status(Server, Database, 
                #    Usuario, Senha,
                   LOGIN, SITUACAO, ID_LIVRO):
    # Conexão para criar o banco de dados 
    dados_conexao = (
    "DRIVER=ODBC Driver 17 for SQL Server;"   # "Driver={SQL Server};"  / "DRIVER=ODBC Driver 17 for SQL Server;"
    "Server="+Server+";"
    "Database="+Database+";"
    # "UID="+Usuario+";"
    # "PWD="+Senha+";"
    "Trusted_Connection=yes;"  # "Encrypt=yes;TrustServerCertificate=yes"  /  "Trusted_Connection=yes;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

    # Crie um cursor
    cursor = conexao.cursor()

    if SITUACAO == 'Emprestado':
        comando_sql = f"""
                        UPDATE BIBLIOTECA_EXPERTISE
                        SET SITUACAO = 'Emprestado',
                            FUNCIONARIO = '{LOGIN}',
                            DATA_EMPRESTIMO = GETDATE()
                        WHERE ID_LIVRO = {ID_LIVRO}"""
        
        cursor.execute(comando_sql)
        # Confirmando as alterações
        conexao.commit()
        print("Alteração realizada com sucesso!")

    elif SITUACAO == 'Disponível':
        comando_sql = f"""
                        UPDATE BIBLIOTECA_EXPERTISE
                        SET SITUACAO = 'Disponível',
                            FUNCIONARIO = NULL,
                            DATA_EMPRESTIMO = NULL
                        WHERE ID_LIVRO = {ID_LIVRO}"""
        
        cursor.execute(comando_sql)
        # Confirmando as alterações
        conexao.commit()
        print("Alteração realizada com sucesso!")

    conexao.close()
    return 


#=== 3º Passo - Inserção de livros ===#
def inserir_livros(Server, Database, 
                #    Usuario, Senha, 
                   LOGIN, TITULO, AUTOR):
    # Conexão para criar o banco de dados 
    dados_conexao = (
    "DRIVER=ODBC Driver 17 for SQL Server;"   # "Driver={SQL Server};"  / "DRIVER=ODBC Driver 17 for SQL Server;"
    "Server="+Server+";"
    "Database="+Database+";"
    # "UID="+Usuario+";"
    # "PWD="+Senha+";"
    "Trusted_Connection=yes;"  # "Encrypt=yes;TrustServerCertificate=yes"  /  "Trusted_Connection=yes;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

    # Crie um cursor
    cursor = conexao.cursor()

    if LOGIN == 'admin' and SENHA == 'Exp2025$':
        comando_sql = f"""
                        INSERT INTO [dbo].[BIBLIOTECA_EXPERTISE]
                            ([TITULO],
                            [AUTOR],
                            [DATA_EMPRESTIMO],
                            [FUNCIONARIO],
                            [SITUACAO])
                        VALUES ('{TITULO}', '{AUTOR}', NULL, NULL, 'Disponível')
                        """
        
        cursor.execute(comando_sql)
        # Confirmando as alterações
        conexao.commit()
        print("Alteração realizada com sucesso!")
    
    else:
        print("Login ou senha incorreta!")

    conexao.close()
    return 


# dados = buscar_livros(Server='10.0.1.66', 
#                       Database='BI_DW_BETA', 
#                       Usuario='rayner.santos', 
#                       Senha='8J1"hP^Kgr}4', 
#                       banco='BIBLIOTECA_EXPERTISE')
# print(dados)

# alterar_status(Server='10.0.1.66', Database='BI_DW_BETA', Usuario='rayner.santos', Senha='8J1"hP^Kgr}4', 
#                 LOGIN=LOGIN, SITUACAO='Emprestado', ID_LIVRO=1)

# inserir_livros(Server='10.0.1.66', Database='BI_DW_BETA', Usuario='rayner.santos', Senha='8J1"hP^Kgr}4', 
#                LOGIN=LOGIN, TITULO='Pesquisa de Mercado', AUTOR='Expertise')