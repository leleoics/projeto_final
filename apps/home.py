import streamlit as st
from apps.maps import region

# # Abrindo imagens locais
# logo_ee = Image.open("./data/thumbnails/ee.png")
# logo_ufpr = Image.open("./data/thumbnails/ufpr.png")
# logo_streamlit = Image.open("./data/thumbnails/streamlit.png")
# logo_github = Image.open("./data/thumbnails/github.png")
# logo_cartografica = Image.open("./data/thumbnails/cartografica.png")


@st.cache(suppress_st_warning=True)
def plot_gif(selection):
    if selection == 1:
        st.image("https://media.giphy.com/media/YLuFnx1KX7a0srNgc2/giphy.gif", width=480, caption="Série histórica da região de Curitiba. Fonte: Autor")
    if selection == 2:
        st.image("https://media.giphy.com/media/7Zgv7DmuOqYZjGdcul/giphy.gif", width=430, caption="Série histórica da Represa do Iraí, Landsat 8 - Combinação: B5, B6, B4. Fonte: Autor")
    return


@st.cache(suppress_st_warning=True)
def plot_image(selection):
    if selection == 'Earth Engine':
        st.image("https://media.giphy.com/media/DREdqwQr7fIkjefTN0/giphy.gif", caption="Google Earth Engine", width=80)
    if selection == 'Github':
        st.image("https://media.giphy.com/media/KSaNOvsbk0KdWkz7J9/giphy.gif", caption="GitHub", width=80)
    if selection == 'Streamlit':
        st.image("https://media.giphy.com/media/cjOSHYWOqfNwyLkRv8/giphy.gif", caption="Streamlit", width=80)
    return

def inicio(title):
    st.title(title)
    st.info("""
    Esta é uma aplicação em desenvolvimento como projeto final do curso de Engenharia Cartografica e de Agrimensura 
    da Universidade Federal do Paraná.   
            """)
    col01, col02 = st.columns([1, 1])
    with col01:
        plot_gif(1)
    with col02:
        plot_gif(2)

    st.markdown("""
    Este projeto está sendo desenvolvido como trabalho de conclusão de curso da Engenharia Cartografica e de Agrimensura, 
    da Universidade Federal do Paraná. O objetivo é desenvolver uma aplicação web com análises temporais sobre o 
    desenvolvimento da cidade de Curitiba e região metropolitana, analisando as Áreas de Preservação Permanentes (APPs) 
    ao entorno das massas d'água, análises do crescimento populacional e também análises sobre o abastecimento de água 
    do Núcleo Urbano Central (NUC).\n
    """)
    if st.checkbox("Visualizar área de estudo") == 1:
        region()
    st.markdown("----")
    st.markdown("Esta aplicação utiliza as ferramentas:\n")
    col11, col12, col13 = st.columns([2, 2, 1])
    with col11:
        plot_image('Github')

    with col12:
        plot_image('Streamlit')

    with col13:
        plot_image('Earth Engine')
 

    # st.markdown("----")
    # col21, col22, col23, col24 = st.columns([1, 1, 1, 1])
    # with col21:
    #     st.image(logo_ufpr, width=150)
    # with col22:
    #     st.markdown("**Universidade Federal do Paraná**")
    #     link1="- [Página inicial](https://www.ufpr.br/portalufpr/)"
    #     link2 ="- [Ciências da Terra](http://www.terra.ufpr.br/portal/)"
    #     st.markdown(link1,unsafe_allow_html=True)
    #     st.markdown(link2,unsafe_allow_html=True)
    # with col23:
    #     st.image(logo_cartografica, width=150)
    # with col24:
    #     st.markdown("**Engenharia Cartográfica e de Agrimensura**")
    #     link3="- [Página inicial](http://www.cartografica.ufpr.br)"
    #     st.markdown(link3,unsafe_allow_html=True)
    return
