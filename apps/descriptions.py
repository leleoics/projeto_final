import streamlit as st


def inicio(titulo):
    st.title(titulo)
    st.markdown("----")
    st.info("""
    Esta é uma aplicação em desenvolvimento como projeto final do curso de Engenharia Cartografica e de Agrimensura 
    da Universidade Federal do Paraná.   
            """)
    st.markdown("""
    O objetivo desta aplicação é apresentar análises realizadas a partir de imagens orbitais, na região de Curitiba.\n
    Foram definidas áreas de represas da grande Curitiba como regiões de estudo, para apresentar séries temporais de imagens.\n
    Além destas regiões, a região de Curitiba também será objeto de estudo, apresentando uma análise sobre o crescimento populacional ao longo dos anos.\n
        Esta é uma aplicação desenvolvida utilizando as ferramentas:.\n
    - Google Earth Engine;\n
    - Streamlit;\n
    - ....
    """)
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

