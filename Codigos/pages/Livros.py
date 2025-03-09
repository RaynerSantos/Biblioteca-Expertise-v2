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
st.write("*Informe as opções desejadas abaixo para solicitar Empréstimo/Devolução do livro desejado.*")

#=== Criar formulário ===#
with st.form(key='alterar_status'):
    SITUACAO_USUARIO = st.selectbox('Selecione a opção desejada', options=['Empréstimo', 'Devolução'])
    ID_LIVRO = st.text_input(label="Insira o ID do livro desejado")
    input_buttom_submit = st.form_submit_button("Enviar")

# Criar um estado de sessão para verificar retorno da solicitação
if "retorno_solicitacao" not in st.session_state:
    st.session_state.retorno_solicitacao = False

# Se o botão for pressionado:
if input_buttom_submit:
    if ID_LIVRO not in dados['ID_LIVRO'].astype(str).values:
        st.warning("ID_LIVRO não existe! Favor digitar um ID_LIVRO válido.")
    else:
        # Salvar os dados no session_state para a próxima página
        st.session_state.SITUACAO_USUARIO = SITUACAO_USUARIO
        st.session_state.ID_LIVRO = ID_LIVRO
        # Redireciona para a página Solicitacao.py
        st.switch_page("pages/Solicitacao.py")
