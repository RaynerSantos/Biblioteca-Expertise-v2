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

# # Configurações da página
# st.set_page_config(layout="centered")  # "wide" / "centered"

#=== Título ===#
st.title("Biblioteca Expertise")

# Criar um estado de sessão para verificar login
if "login_sucesso" not in st.session_state:
    st.session_state.login_sucesso = False

# Formulário de login
with st.form(key="login"):
    LOGIN = st.text_input(label="Insira o seu login de acesso")
    SENHA = st.text_input(label="Insira a sua senha", type='password')
    input_buttom_submit = st.form_submit_button("Entrar")


# Se o botão for pressionado, verifica login
if input_buttom_submit:
    df_logins = buscar_livros(Server='LAPTOP-O3PIH7AD\SQLEXPRESS01',  # 10.0.1.66
                    Database='BIBLIOTECA_EXPERTISE',                  # BI_DW_BETA
                    # Usuario='LAPTOP-O3PIH7AD\rayne',                  # rayner.santos
                    # Senha='',                                         # 8J1"hP^Kgr}4
                    banco='BIBLIOTECA_EXPERTISE_LOGINS')
    if ((df_logins['LOGIN'] == LOGIN) & (df_logins['SENHA'] == SENHA)).any():
        st.session_state.login_sucesso = True  # Define o estado do login como verdadeiro
        st.session_state.LOGIN = LOGIN  # Salva o usuário na sessão
        st.rerun()  # Recarrega a página para aplicar a mudança
    else:
        st.warning("Login ou senha incorretos!")

# Se login for bem-sucedido, redireciona para a página de livros e ou página do Administrador
if st.session_state.login_sucesso and LOGIN == 'admin':
    st.switch_page("pages/Administrador.py")

elif st.session_state.login_sucesso:
    st.switch_page("pages/Livros.py")

