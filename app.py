import streamlit as st

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
aplications = ["Teste", "Sobre"]
st.sidebar.radio("Ir para: ", aplications)

