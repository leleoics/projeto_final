import streamlit as st


def plot_gif(selection):
    if selection == 1:
        st.image("https://media.giphy.com/media/YLuFnx1KX7a0srNgc2/giphy.gif", width=480, caption="Série histórica da região de Curitiba. Fonte: Autor")
    if selection == 2:
        st.image("https://media.giphy.com/media/7Zgv7DmuOqYZjGdcul/giphy.gif", width=430, caption="Série histórica da Represa do Iraí, Landsat 8 - Combinação: B5, B6, B4. Fonte: Autor")
    return


def plot_image(selection):
    if selection == 'Earth Engine':
        st.image("https://media.giphy.com/media/DREdqwQr7fIkjefTN0/giphy.gif", caption="Google Earth Engine", width=80)
    if selection == 'Github':
        st.image("https://media.giphy.com/media/KSaNOvsbk0KdWkz7J9/giphy.gif", caption="GitHub", width=80)
    if selection == 'Streamlit':
        st.image("https://media.giphy.com/media/cjOSHYWOqfNwyLkRv8/giphy.gif", caption="Streamlit", width=80)
    if selection == 'Detecção':
        st.image("https://media.giphy.com/media/8XpXWrNtQsqzWjws6R/giphy.gif", width=170)
    return

def inicio():
    with st.expander('Ver mais:'):
        # col01, col02 = st.columns([1, 1])
        # with col01:
        #     plot_gif(1)
        # with col02:
        #     plot_gif(2)
        st.markdown("""<p  style='text-align: justify; color: #31333F;'>
        <b>- </b>Este é um projeto desenvolvido como trabalho de conclusão de curso da Engenharia Cartografica e de Agrimensura, 
        da Universidade Federal do Paraná.</p>
        """, unsafe_allow_html=True)

    st.markdown("""<h6  style='text-align: justify; color: #31333F;'>
    Detector de Mudanças é uma ferramenta que permite detectar mudanças na superfície da Terra 🌎 através de imagens orbitais,
    onde é possível detectar alterações entre duas épocas distintas de sua escolha.
    </h6>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    <b>- </b> Disponível técnicas de detecção de mudanças para os seguintes fenômenos:
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    🌊 Água 
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    🌳 Vegetação 
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    🌆 Urbanização 
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    <b>- </b>Para ir para a aplicação seguir os seguintes passos:</p>""", unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    🔼 Ver Menu
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""<p  style='text-align: justify; color: #31333F;'>
    ⏬ Aplicação
    </p>
    """, unsafe_allow_html=True)
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
