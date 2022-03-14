import streamlit as st
from apps.home import inicio
from apps.descriptions import sobre
from apps.selector import parametros
import ee
from PIL import Image

#CONFIGURANDO O STREAMLIT:
#- Passando o título da página;
#- Ícone;
#- Definido o layout wide;
#- Barra lateral sempre aberta;
logo = Image.open("./data/thumbnails/ufpr_b.jpg")
st.set_page_config(
page_title="TCC",
page_icon=logo,
layout="wide",
menu_items={
'Get help': 'https://github.com/leleoics/projeto_final'})
#INICIALIZANDO O GOOGLE EARTH ENGINE:
service_account = "projetofinal@projetofinal-340114.iam.gserviceaccount.com"
key_path = "./data/restricted/projetofinal-340114-5db12cbc8740.json"
credentials = ee.ServiceAccountCredentials(service_account, key_path)
ee.Initialize(credentials)

#CABEÇALHO COM ACESSO AOS APPs
st.markdown("----")
menu = st.expander('Ver Menu')
with menu:
    pagina = st.radio(
    "Selecione a página: ",
    ('Página Inícial', 'Aplicação', 'Sobre'))

st.markdown("----")
if pagina == 'Página Inícial':
    inicio(pagina)


if pagina == 'Aplicação':
    parametros()


if pagina == 'Sobre':
    sobre(pagina)