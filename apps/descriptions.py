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
    st.info("""
    Esta é uma aplicação em desenvolvimento como projeto final do curso de Engenharia Cartografica e de Agrimensura 
    da Universidade Federal do Paraná.   
            """)
    col01, col02 = st.columns([1, 1])
    with col01:
        st.image("https://media.giphy.com/media/YLuFnx1KX7a0srNgc2/giphy.gif", width=480, caption="Série histórica da região de Curitiba. Fonte: Autor")
    with col02:
        st.image("https://media.giphy.com/media/7Zgv7DmuOqYZjGdcul/giphy.gif", width=430, caption="Série histórica da Represa do Iraí, Landsat 8 - Combinação: B5, B6, B4. Fonte: Autor")

    # tabela = """
    # Exemplo   | Valor do exemplo
    # --------- | :------:
    # Exemplo 1 | R$ 10
    # Exemplo 2 | R$ 8
    # Exemplo 3 | R$ 7
    # Exemplo 4 | R$ 8
    
    # """
    # st.markdown(tabela, unsafe_allow_html=True)
    st.markdown("""
    O objetivo desta aplicação é apresentar análises realizadas a partir de imagens orbitais, na região de Curitiba.\n
    Foram definidas áreas de represas da grande Curitiba como regiões de estudo, para apresentar séries temporais de imagens.\n
    Além destas regiões, a região de Curitiba também será objeto de estudo, apresentando uma análise sobre o crescimento populacional ao longo dos anos.\n
    Esta aplicação utiliza as ferramentas:\n
    """)
    col11, col12, col13 = st.columns([2, 2, 1])
    with col11:
        st.image(logo_github, caption="GitHub", width=80)
    with col12:
        st.image(logo_streamlit, caption="Streamlit", width=80)
    with col13:
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

