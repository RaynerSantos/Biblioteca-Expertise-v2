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
if "SITUACAO_USUARIO" not in st.session_state or "ID_LIVRO" not in st.session_state:
    st.warning("Nenhuma solicitação foi realizada! Volte à página anterior.")
    st.stop()

st.title("Retorno da solicitação")

if st.session_state.SITUACAO_USUARIO == 'Empréstimo' and st.session_state.dados.loc[int(st.session_state.ID_LIVRO)-1,'SITUACAO'] == 'Disponível':
    alterar_status(Server='LAPTOP-O3PIH7AD\SQLEXPRESS01',  # 10.0.1.66
                   Database='BIBLIOTECA_EXPERTISE',        # BI_DW_BETA
                #    Usuario='LAPTOP-O3PIH7AD\rayne',        # rayner.santos
                #    Senha='',                               # 8J1"hP^Kgr}4 
                   LOGIN=st.session_state.LOGIN, 
                   SITUACAO='Emprestado', 
                   ID_LIVRO=st.session_state.ID_LIVRO)
    st.write(f"Usuário: **{st.session_state.LOGIN}**")
    st.write(f"ID do Livro Selecionado: **{st.session_state.ID_LIVRO}**")
    st.write(f"Título: **{st.session_state.dados.loc[int(st.session_state.ID_LIVRO)-1,'TITULO']}**")
    st.write(f"Autor: **{st.session_state.dados.loc[int(st.session_state.ID_LIVRO)-1,'AUTOR']}**")
    st.write(f"Ação: **{st.session_state.SITUACAO_USUARIO}**")

    st.write("")
    st.success("Solicitação registrada com sucesso!")
    st.write("Você já pode pegar o livro na estante da Biblioteca Expertise")

elif st.session_state.SITUACAO_USUARIO == 'Devolução':
    alterar_status(Server='LAPTOP-O3PIH7AD\SQLEXPRESS01',  # 10.0.1.66
                   Database='BIBLIOTECA_EXPERTISE',        # BI_DW_BETA
                #    Usuario='LAPTOP-O3PIH7AD\rayne',        # rayner.santos
                #    Senha='',                               # 8J1"hP^Kgr}4 
                   LOGIN=st.session_state.LOGIN, 
                   SITUACAO='Disponível', 
                   ID_LIVRO=st.session_state.ID_LIVRO)
    st.write(f"Usuário: **{st.session_state.LOGIN}**")
    st.write(f"ID do Livro Selecionado: **{st.session_state.ID_LIVRO}**")
    st.write(f"Título: **{st.session_state.dados.loc[int(st.session_state.ID_LIVRO)-1,'TITULO']}**")
    st.write(f"Autor: **{st.session_state.dados.loc[int(st.session_state.ID_LIVRO)-1,'AUTOR']}**")
    st.write(f"Ação: **{st.session_state.SITUACAO_USUARIO}**")

    st.write("")
    st.success("Solicitação registrada com sucesso!")
    st.write("Favor devolver o livro na estante da Biblioteca Expertise")
else:
    st.warning("Livro desejado não está disponível no momento.")
    



