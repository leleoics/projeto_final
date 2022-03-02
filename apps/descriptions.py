import streamlit as st
from apps.maps import region

def area_interesse(titulo):
    st.title(titulo)
    st.markdown("""
    O estudo é realizado na região definida como Núcleo Urbano Central (NUC) da Região metropolitana de Curitiba.\n
    **Municípios que compõem o (NUC)**: Almirante Tamandaré, Araucária, Campina Grande do Sul, 
    Campo Largo, Campo Magro, Colombo, Curitiba, Fazenda Rio Grande, Itaperuçu, Pinhais, Piraquara, Quatro Barras, 
    Rio Branco do Sul e São José dos Pinhais.
    """)
    if st.checkbox("Visualizar mapa da área de estudo:") == 1:
        st.markdown("----")
        region()
        st.markdown("----")
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