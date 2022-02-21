import streamlit as st
from apps.descriptions import inicio, sobre
from apps.mapas_base import reservatorios
import ee
from PIL import Image

#CONFIGURANDO O STREAMLIT:
#- Passando o título da página;
#- Ícone;
#- Definido o layout wide;
#- Barra lateral sempre aberta;
logo = Image.open("./data/ufpr_b.jpg")
st.set_page_config(
page_title="TCC",
page_icon=logo,
layout="wide")
#INICIALIZANDO O GOOGLE EARTH ENGINE:
service_account = "projetofinal@projetofinal-340114.iam.gserviceaccount.com"
key_path = "./data/projetofinal-340114-5db12cbc8740.json"
credentials = ee.ServiceAccountCredentials(service_account, key_path)
ee.Initialize(credentials)


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
