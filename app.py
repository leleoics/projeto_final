import streamlit as st
from apps.home import inicio
from apps.descriptions import sobre
from apps.selector import parametros
from apps.home import plot_image
import ee
from PIL import Image

#CONFIGURANDO O STREAMLIT:
#- Passando o título da página;
#- Ícone;
#- Definido o layout wide;
#- Barra lateral sempre aberta;
logo = Image.open("./data/thumbnails/detec_thumb.png")
st.set_page_config(
page_title="Detector de Mudanças",
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
col01, col02, col03 = st.columns([1, 3, 1])
with col01:
    menu = st.expander('Menu',expanded=True)
    with menu:
        pagina = st.radio(
        "Selecione a página: ",
        ('Página Inícial', 'Detecção de Mudança', 'Sobre'))
    # st.markdown("""
    # <h5  style='text-align: center; color: #31333F;'>
    # {}</h5>
    # """.format(pagina) , unsafe_allow_html=True)

with col02:
    cabecalho = Image.open("./data/thumbnails/cabecalho.png")
    st.image(cabecalho, use_column_width=True)
with col03:
    plot_image('Detecção')

st.markdown("----")
if pagina == 'Página Inícial':
    inicio()


if pagina == 'Detecção de Mudança':
    parametros()


if pagina == 'Sobre':
    sobre(pagina)