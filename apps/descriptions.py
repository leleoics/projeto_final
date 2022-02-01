import streamlit as st
from io import StringIO


def inicio(titulo):
    st.title(titulo)
    st.markdown("----")
    st.info("""
    Esta aplicação esta sendo desenvolvida como projeto final do curso de Engenharia Cartografica e de Agrimensura 
    da Universidade Federal do Paraná.   
            """)
    st.markdown("""
    Aqui são apresentados temas de estudos realizados com dados abertos, ferramentas gratuítas e direcionados a região
    imediata de Curitiba.\n
    **São apresentado ferramentas como:**\n
    - Google Earth Engine; .... COMPLEMENTAR\n
    **A partir disso foi possível construir estudos sobre:**\n
    - Reservatórios de Água;\n
    - Crescimento populacional;\n
    ... COMPLEMENTAR
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

