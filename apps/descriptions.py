import streamlit as st
from PIL import Image
import base64



logo_ee = Image.open("./data/brand_ee.png")
logo_ufpr = Image.open("./data/brand_ufpr.png")
logo_streamlit = Image.open("./data/brand_streamlit.png")
logo_github = Image.open("./data/brand_github.png")
logo_cartografica = Image.open("./data/brand_cartografica.png")


def inicio(titulo):
    st.title(titulo)
    st.markdown("----")
    st.info("""
    Esta é uma aplicação em desenvolvimento como projeto final do curso de Engenharia Cartografica e de Agrimensura 
    da Universidade Federal do Paraná.   
            """)
    st.image("https://media.giphy.com/media/PdNKkVOwmPwIY7VT03/giphy.gif", width=480, caption="Série histórica da região de Curitiba. Fonte: Autor")
    #Inserir outro gif dp lado
    st.markdown("""
    O objetivo desta aplicação é apresentar análises realizadas a partir de imagens orbitais, na região de Curitiba.\n
    Foram definidas áreas de represas da grande Curitiba como regiões de estudo, para apresentar séries temporais de imagens.\n
    Além destas regiões, a região de Curitiba também será objeto de estudo, apresentando uma análise sobre o crescimento populacional ao longo dos anos.\n
    Esta aplicação utiliza as ferramentas:\n
    """)
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.image(logo_github, caption="GitHub", width=80)
    with col2:
        st.image(logo_streamlit, caption="Streamlit", width=80)
    with col3:
        st.image(logo_ee, caption="Google Earth Engine", width=80)

    st.markdown("----")
    col21, col22, col23, col24 = st.columns([1, 1, 1, 1])
    with col21:
        st.image(logo_ufpr, width=150)
    with col22:
        st.markdown("**Universidade Federal do Paraná**")
        link1="- [Página inicial](https://www.ufpr.br/portalufpr/)"
        link2 ="- [Ciências da Terra](http://www.terra.ufpr.br/portal/)"
        st.markdown(link1,unsafe_allow_html=True)
        st.markdown(link2,unsafe_allow_html=True)
    with col23:
        st.image(logo_cartografica, width=150)
    with col24:
        st.markdown("**Engenharia Cartográfica e de Agrimensura**")
        link3="- [Página inicial](http://www.cartografica.ufpr.br)"
        st.markdown(link3,unsafe_allow_html=True)
    return


def sobre(titulo):
    st.title(titulo)
    st.markdown("""
    **Autor:** Leonardo de Oliveira Melo\n
    **Formação:** Graduando em Eng. Cartógrafica e de Agrimensura\n
    **Instituição:** Universidade Federal do Paraná\n
    **Linkedin:** https://www.linkedin.com/in/leonardo-oliveira-melo-287593164/\n
    **GitHub:** https://github.com/leleoics\n
    **Projeto:** Desenvolver aplicação interativa com estudos da região imediata de Curitba\n    
    **Status:** Em desenvolvimento    
    """)

