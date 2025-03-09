# python -m streamlit run Login.py
import pandas as pd
import pyodbc
import streamlit as st
from Funcoes_Biblioteca import buscar_livros, alterar_status, inserir_livros

# CSS personalizado
st.markdown(
    """
    <style>
    /* Cor de fundo da página */
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }
    
    /* Cor de fundo do cabeçalho */
    [data-testid="stHeader"] {
        background-color: #000000;
    }

    /* Cor de fundo da barra lateral */
    [data-testid="stSidebar"] {
        background-color: #333333;
    }

    /* Cor do título */
    h1 {
        color: #FFFFFF; /* Laranja avermelhado */
        text-align: center;
    }

    /* Cor do subtítulo */
    h2 {
        color: #FFD700; /* Dourado */
    }

    /* Cor do texto normal */
    p, span {
        color: #FFFFFF; /* Branco */
    }

    /* Cor dos botões */
    button {
        background-color: #20541B !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Se o usuário não estiver autenticado, redireciona para a página inicial
if "login_sucesso" not in st.session_state or not st.session_state.login_sucesso:
    st.warning("Você precisa fazer login!")
    st.stop()

# Criar um estado de sessão para verificar login
if "solicitacao_admin" not in st.session_state:
    st.session_state.solicitacao_admin = False

# Título da nova página
st.title("Biblioteca Expertise")
st.write("")  # Linha vazia
st.write(f"Bem-vindo, **{st.session_state.LOGIN}**!")
st.write("")  # Linha vazia
st.write("Tabela com informação dos livros (Disponível / Emprestado)")

# Buscar dados da biblioteca
dados = buscar_livros(Server='LAPTOP-O3PIH7AD\SQLEXPRESS01',  # 10.0.1.66
                      Database='BIBLIOTECA_EXPERTISE',        # BI_DW_BETA
                    #   Usuario='LAPTOP-O3PIH7AD\rayne',        # rayner.santos
                    #   Senha='',                               # 8J1"hP^Kgr}4
                      banco='BIBLIOTECA_EXPERTISE')
st.session_state.dados = dados

# Exibir os dados
st.dataframe(dados, width=1500, height=500, hide_index=True)

st.write("")  # Linha vazia
st.write("*Informe abaixo o título e autor do livro que deseja incluir na Biblioteca Expertise*")

#=== Criar formulário ===#
with st.form(key='inserir_livros'):
    TITULO = st.text_input(label="Informe o nome do Título do livro que deseja incluir")
    AUTOR = st.text_input(label='Informe o nome do Autor do livro que deseja incluir')
    input_buttom_submit = st.form_submit_button("Enviar")
    st.session_state.TITULO = TITULO
    st.session_state.AUTOR = AUTOR

# Se o botão for pressionado:
if input_buttom_submit:
    st.session_state.solicitacao_admin = True  # Define o estado do solicitacao do administrador como verdadeiro
    # Redireciona para a página Solicitacao_admin.py
    st.switch_page("pages/Solicitacao_admin.py")