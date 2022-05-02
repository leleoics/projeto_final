import streamlit as st
from PIL import Image

def plot_gif(selection):
    if selection == 1:
        st.image("https://media.giphy.com/media/SmydthqIu0FjltBZVc/giphy.gif", use_column_width=True, caption="Guia para aplicação.")
    if selection == 2:
        st.image("https://media.giphy.com/media/7Zgv7DmuOqYZjGdcul/giphy.gif", use_column_width=True, caption="Série histórica da Represa do Iraí, Landsat 8 - Combinação: B5, B6, B4. Fonte: Autor")
    return


def plot_image(selection):
    if selection == 'Earth Engine':
        st.image("https://media.giphy.com/media/DREdqwQr7fIkjefTN0/giphy.gif", caption="Google Earth Engine", width=80)
    if selection == 'Github':
        st.image("https://media.giphy.com/media/KSaNOvsbk0KdWkz7J9/giphy.gif", caption="GitHub", width=80)
    if selection == 'Streamlit':
        st.image("https://media.giphy.com/media/cjOSHYWOqfNwyLkRv8/giphy.gif", caption="Streamlit", width=80)
    if selection == 'Detecção':
        st.image("https://media.giphy.com/media/8XpXWrNtQsqzWjws6R/giphy.gif", width=140)
    if selection == 'vegetacao':
        st.image("https://media.giphy.com/media/SGDJDSFqDS549QKglO/giphy.gif", use_column_width=True)
    if selection == 'agua':
        st.image("https://media.giphy.com/media/O4kZMkFcEonlAMdkEP/giphy.gif", use_column_width=True)
    if selection == 'urbano':
        st.image("https://media.giphy.com/media/CnzTCZyFzzkLsiQ1ar/giphy.gif", use_column_width=True)
    return

def inicio():

    st.markdown("""<h5  style='text-align: justify; color: #31333F;'>
    O que é:</h5>
    """, unsafe_allow_html=True)

    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    Detector de Mudanças é uma ferramenta que permite detectar mudanças na superfície da Terra através de imagens orbitais,
    onde é possível detectar alterações entre duas épocas distintas de sua escolha.
    </p>
    """, unsafe_allow_html=True)



    st.markdown("""<h6  style='text-align: justify; color: #31333F;'>
    📌 Disponível técnicas de detecção de mudanças para os seguintes fenômenos:
    </h6>
    """, unsafe_allow_html=True)
    col01, col02, col03 = st.columns([1, 1, 1])
    with col01:
        # plot_image('vegetacao')
        vegetacao = Image.open("./data/thumbnails/veg.png")
        st.image(vegetacao, use_column_width=True)
        with st.expander('Saber mais'):
            st.markdown("Técnica de detecção por diferença de (NDVI)")
            st.video('https://youtu.be/Vv09DKTAI20')

    with col02:
        # plot_image('agua')
        agua = Image.open("./data/thumbnails/agua.png")
        st.image(agua, use_column_width=True)
        with st.expander('Saber mais'):
            st.markdown("Técnica de detecção por diferença de (NDWI)")
            st.video('https://youtu.be/Tot280Elbck')

    with col03:
        # plot_image('urbano')
        urbano = Image.open("./data/thumbnails/urbano.png")
        st.image(urbano, use_column_width=True)
        with st.expander('Saber mais', ):
            st.markdown("Técnica de detecção por (RCEN)")
            st.video('https://youtu.be/2oxlqsuaRBo')

    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    <b>  </b> </p>""", unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    <b>  </b> </p>""", unsafe_allow_html=True)

    col11, col12 = st.columns([5, 1])
    with col11:
            st.markdown("""<h5  style='text-align: justify; color: #31333F;'>
        📑 Sobre o projeto</h5>
        """, unsafe_allow_html=True)

            st.markdown("""<p  style='text-align: justify; color: #31333F;'>
            Este é um projeto desenvolvido como trabalho de conclusão de curso da Engenharia Cartografica e de Agrimensura, 
        da Universidade Federal do Paraná. O objetivo da aplicação é disponibilizar ao usuário uma plataforma para detectar 
        mudanças a partir de uma série temporal de imagens através do processamento de imagens em nuvem no Google Earth 
        Engine e pode ser utilizado por alguém que deseje mapear mudanças entre épocas ou para uso educacional.</p>
        """, unsafe_allow_html=True)

            st.markdown("""
            Página do Curso: [Eng. Cart. e de Agrim - UFPR](http://www.cartografica.ufpr.br/)""")

    with col12:
        st.markdown("""<h6  style='text-align: center; color: #31333F;'>
        Instituição</h6>
        """, unsafe_allow_html=True)
        ufpr = Image.open("./data/thumbnails/institucional.png")
        st.image(ufpr, use_column_width=True)

    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    </p>""", unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    </p>""", unsafe_allow_html=True)

    st.markdown("""<h5  style='text-align: justify; color: #31333F;'>
    🎥 Vídeos:</h5>""", unsafe_allow_html=True)
    with st.expander('Ver mais'):
        col21, col22 = st.columns([1, 1])
        with col21:
            st.markdown("""<h5  style='text-align: center; color: #31333F;'>
            <b>Exemplo de uso da aplicação - Reservatório de água do Iraí no Paraná</b>
        </h5>""", unsafe_allow_html=True)
            st.video('https://youtu.be/3QxgN4vBQVg')

            st.markdown("""<h5  style='text-align: center; color: #31333F;'>
            <b>Técnica de detecção de mudança por diferença de NDWI</b>
        </h5>""", unsafe_allow_html=True)
            st.video('https://youtu.be/Tot280Elbck')

        with col22:
            st.markdown("""<h5  style='text-align: center; color: #31333F;'>
           <b>Técnica de detecção de mudança por diferença de NDVI</b>
        </h5>""", unsafe_allow_html=True)
            st.video('https://youtu.be/Vv09DKTAI20')

            st.markdown("""<h5  style='text-align: center; color: #31333F;'>
            <b>Técnica de detecção de mudança por RCEN</b>
        </h5>""", unsafe_allow_html=True)
            st.video('https://youtu.be/2oxlqsuaRBo')



    st.markdown("----")
    st.markdown("""<h6  style='text-align: center; color: #31333F;'>
    Esta aplicação utiliza as ferramentas:
    </h6>""", unsafe_allow_html=True)
    col21, col22, col23 = st.columns([2, 2, 1])
    with col21:
        plot_image('Github')

    with col22:
        plot_image('Streamlit')

    with col23:
        plot_image('Earth Engine')
 
    return
