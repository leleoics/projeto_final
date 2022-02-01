import streamlit as st
from apps.descriptions import inicio, sobre
from apps.mapas_base import reservatorios

#CONFIGURANDO O STREAMLIT:
#- Passando o título da página;
#- Ícone;
#- Definido o layout wide;
#- Barra lateral sempre aberta;
st.set_page_config(
page_title="Leonardo",
layout="wide",
initial_sidebar_state="expanded")

# BARRA LATERAL
# - Inserindo título;
# - Inserindo botões de navegação;
st.sidebar.title("Navegação")
aplicacoes = ["Início", "Reservatórios de água", "Sobre"]
selecao = st.sidebar.radio("Ir para: ", aplicacoes)

# INÍCIO
if selecao == "Início":
    inicio(selecao)

# RESERVATÓRIOS DE ÁGUA
if selecao == "Reservatórios de água":
    reservatorios(selecao)

# SOBRE
if selecao == "Sobre":
    sobre(selecao)


