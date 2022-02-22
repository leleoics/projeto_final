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
'Get Help': 'https://www.extremelycoolapp.com/help'})
#INICIALIZANDO O GOOGLE EARTH ENGINE:
service_account = "projetofinal@projetofinal-340114.iam.gserviceaccount.com"
key_path = "./data/projetofinal-340114-5db12cbc8740.json"
credentials = ee.ServiceAccountCredentials(service_account, key_path)
ee.Initialize(credentials)

# Testando novo Layout com cabeçalho
col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
with col1:
    pagina1 = st.button("Início", help="Ir para página inicial")

with col2:
    pagina2 = st.button("Reservatórios de Água", help="Análises sobre os reservatórios de água.")

with col3:
    pagina3 = st.button("Crescimento populacional", help="Análises sobre o crescimento populacional.", disabled=True)

with col4:
    pagina4 = st.button("Relatórios por ano", help="Acessar catálogo de relatórios.", disabled=True)
    
with col5:
    pagina5 = st.button("Metadados", help="Acessar metadados do projeto.", disabled=True)

with col6:
    pagina6 = st.button("Sobre", help="Informações sobre o projeto.")
    
verificacao = (pagina2, pagina3, pagina4, pagina5, pagina6) #Verificação de páginas ativas
st.markdown("----")
if sum(verificacao) == 0: #Se outra página estiver ativa, não entra nesta condição ou seja, fecha a aba
    inicio('Início')
if pagina2 == 1:
    reservatorios('Reservatórios de Água')
    st.markdown("Entrou apenas aqui")
if pagina6 == 1:
    sobre('Sobre')
