import streamlit as st


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
        st.image("https://media.giphy.com/media/SGDJDSFqDS549QKglO/giphy.gif", width=200)
    if selection == 'agua':
        st.image("https://media.giphy.com/media/O4kZMkFcEonlAMdkEP/giphy.gif", width=200)
    if selection == 'urbano':
        st.image("https://media.giphy.com/media/CnzTCZyFzzkLsiQ1ar/giphy.gif", width=200)
    return

def inicio():
    with st.expander('Ver mais:'):
        st.markdown("""<p  style='text-align: justify; color: #31333F;'>
        <b>- </b>Este é um projeto desenvolvido como trabalho de conclusão de curso da Engenharia Cartografica e de Agrimensura, 
        da Universidade Federal do Paraná.</p>
        """, unsafe_allow_html=True)

    st.markdown("""<h6  style='text-align: justify; color: #31333F;'>
    Detector de Mudanças é uma ferramenta que permite detectar mudanças na superfície da Terra através de imagens orbitais,
    onde é possível detectar alterações entre duas épocas distintas de sua escolha.
    </h6>
    """, unsafe_allow_html=True)
    st.markdown("""<h6  style='text-align: justify; color: #31333F;'>
    📌 Disponível técnicas de detecção de mudanças para os seguintes fenômenos:
    </h6>
    """, unsafe_allow_html=True)
    col01, col02, col03 = st.columns([2, 2, 1])
    with col01:
        plot_image('vegetacao')
    with col02:
        plot_image('agua')
    with col03:
        plot_image('urbano')
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    ----</p>""", unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    <b>  </b> </p>""", unsafe_allow_html=True)
    st.markdown("""<h6  style='text-align: justify; color: #31333F;'>
    📎 Para ir para a aplicação seguir os passos do vídeo a seguir:</h6>""", unsafe_allow_html=True)
    video_inicio = open('./data/thumbnails/inicio.mp4','rb')
    video_inicio_bytes = video_inicio.read()
    st.video(video_inicio_bytes, format="video/mp4")
    st.markdown("----")
    st.markdown("""<h6  style='text-align: center; color: #31333F;'>
    Esta aplicação utiliza as ferramentas:
    </h6>""", unsafe_allow_html=True)
    col11, col12, col13 = st.columns([2, 2, 1])
    with col11:
        plot_image('Github')

    with col12:
        plot_image('Streamlit')

    with col13:
        plot_image('Earth Engine')
 
    return
