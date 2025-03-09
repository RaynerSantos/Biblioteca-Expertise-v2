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

# Verifica se o usuário chegou corretamente na página
if "solicitacao_admin" not in st.session_state:
    st.warning("Nenhuma solicitação foi realizada! Volte à página anterior.")
    st.stop()

st.title("Retorno da solicitação")

if st.session_state.solicitacao_admin:
    inserir_livros(Server='LAPTOP-O3PIH7AD\SQLEXPRESS01',  # 10.0.1.66
                   Database='BIBLIOTECA_EXPERTISE',        # BI_DW_BETA
                #    Usuario='LAPTOP-O3PIH7AD\rayne',        # rayner.santos
                #    Senha='',                               # 8J1"hP^Kgr}4
                   LOGIN=st.session_state.LOGIN, 
                   TITULO=st.session_state.TITULO, 
                   AUTOR=st.session_state.AUTOR)
    
    st.write(f"Usuário: **{st.session_state.LOGIN}**")
    st.write(f"Título: **{st.session_state.TITULO}**")
    st.write(f"Autor: **{st.session_state.AUTOR}**")
    st.write(f"Ação: **Inserção de novo livro**")

    st.success("Solicitação registrada com sucesso!")
