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
layout="wide",
initial_sidebar_state="expanded",
menu_items={
'Get help': 'https://github.com/leleoics/projeto_final'})
#INICIALIZANDO O GOOGLE EARTH ENGINE:
service_account = "projetofinal@projetofinal-340114.iam.gserviceaccount.com"
key_path = "./data/projetofinal-340114-5db12cbc8740.json"
credentials = ee.ServiceAccountCredentials(service_account, key_path)
ee.Initialize(credentials)

# Cabeçalho com botões de navegação
st.markdown("----")
menu = st.expander('Ver Menu')
with menu:
    pagina = st.radio(
    "Selecione a página: ",
    ('Página Inícial', 'Reservatórios de Água', 'Crescimento populacional', 'Relatórios por ano', 'Metadados', 'Sobre'))

st.markdown("----")
if pagina == "Página Inícial":
    inicio('Início')
if pagina == 'Reservatórios de Água':
    reservatorios('Reservatórios de Água')
if pagina == 'Crescimento populacional':
    st.markdown("Em desenvolvimento")
    st.markdown("Aqui será apresentado mapas com operações de sig, censo por ano e gráficos mostrando o crescimento populacional")
if pagina == 'Relatórios por ano':
    st.markdown("Em desenvolvimento")
    st.markdown("Aqui será possível visualizar análises e baixar um relatório pdf com as informações de cada ano")
if pagina == 'Metadados':
    st.markdown("Em desenvolvimento")
    st.markdown("Aqui será possível visualizar os metadados e baixar e, pdf.")
if pagina == 'Sobre':
    sobre('Sobre')
