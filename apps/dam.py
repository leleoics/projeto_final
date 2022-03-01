import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import streamlit as st
import geemap.foliumap as geemap
import folium
import ee


def folium_static(fig, width=890, height=500):
    if isinstance(fig, folium.Map):
        fig = folium.Figure().add_child(fig)
    return components.html(fig.render(), height=(fig.height or height), width=width)

#Linha abaixo retorna JSON com informações das imagens filtradas pela nuvem e pela localização
# colecao = ee.ImageCollection.load('LANDSAT/LC08/C01/T1_RT_TOA').filterMetadata('CLOUD_COVER', 'less_than', 2).filterBounds(ee_area_estudo)


def reservatorios(titulo):
    st.title(titulo)
    st.markdown("----")
    st.markdown("Nesta seção é possível encontrar uma análise temporal dos reservatórios da região de Curitiba.")
    # Parâmetros de estilo para a APA #visualizar depois com linha dotted
    vis_params_apa = {'color': '#228B22', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 2, 'lineType': 'dotted', 'fillColorOpacity': 0.1}
# Parâmetros de estilo para o reservatório
    vis_params_reserv = {'color': '#9cc0f9', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 1, 'lineType': 'solid', 'fillColorOpacity': 0.15}
    # Paleta de cores em comum 
    palette = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    # Carregando dados e convertendo para objetos ee
    geojson_area_estudo = "./data/layers_dam/area_estudo.geojson"
    ee_area_estudo = geemap.geojson_to_ee(geojson_area_estudo)

    #                       Irai
    geojson_reserv_irai = "./data/layers_dam/reserv_irai.geojson"
    geojson_APA_irai = "./data/layers_dam/APA_irai.geojson"
    ee_APA_iai = geemap.geojson_to_ee(geojson_APA_irai)
    ee_reserv_irai = geemap.geojson_to_ee(geojson_reserv_irai)

    #                     Passauna
    geojson_reserv_passauna = "./data/layers_dam/reserv_passauna.geojson"
    geojson_APA_passauna = "./data/layers_dam/APA_passauna.geojson"
    ee_APA_passauna = geemap.geojson_to_ee(geojson_APA_passauna)
    ee_reserv_passauna = geemap.geojson_to_ee(geojson_reserv_passauna)


    #                     Piraquara I
    geojson_reserv_piraquaraI = "./data/layers_dam/reserv_piraquara_I.geojson"
    geojson_APA_piraquara = "./data/layers_dam/APA_piraquara.geojson"
    ee_APA_piraquara = geemap.geojson_to_ee(geojson_APA_piraquara)
    ee_reserv_piraquara = geemap.geojson_to_ee(geojson_reserv_piraquaraI)


    #                     Piraquara II
    geojson_reserv_piraquaraII = "./data/layers_dam/reserv_piraquara_II.geojson"
    geojson_APA_piraquara = "./data/layers_dam/APA_piraquara.geojson"
    ee_APA_piraquara_II = geemap.geojson_to_ee(geojson_APA_piraquara)
    ee_reserv_piraquara_II = geemap.geojson_to_ee(geojson_reserv_piraquaraII)

    
    #                      Rio Verde
    geojson_reserv_rioverde = "./data/layers_dam/reserv_rio_verde.geojson"
    geojson_APA_rioverde = "./data/layers_dam/APA_rio_verde.geojson"
    ee_APA_rio_verde = geemap.geojson_to_ee(geojson_APA_rioverde)
    ee_reserv_rio_verde = geemap.geojson_to_ee(geojson_reserv_rioverde)
    col11, col21 = st.columns([2, 1])

    tabela = """
    Represas     | Inauguração  | Bairro atendimento | Capacidade(m³)   |
    ------------ | :----------: | :----------------: |  :-------------: |
    Iraí         |     199x     |      Preencher     |   Preencher      |
    Passaúna     |     1986     |      Preencher     |   Preencher      |
    Piraquara I  |     1979     |      Preencher     |   23.000.000     |
    Piraquara II |     2008     |      Preencher     |   21.000.000     |
    Rio Verde    |     199x     |      Preencher     |   Preencher      | 
    """
    df_volume = {'Iraí':0,'Passaúna':0, 'Piraquara I':23, 'Piraquara II':21, 'Rio Verde':0}
    with col11:
        st.markdown(tabela, unsafe_allow_html=True)
    with col21:
        st.markdown("Capacidade (m³) dos reservatórios de água:")
        fig, ax = plt.subplots()
        ax.bar(df_volume.keys(), df_volume.values(), color="Maroon")
        st.pyplot(fig)
    st.markdown('')
    col12, col22 = st.columns([3, 1])
    with col22:
        local = st.selectbox("Selecione o local para visualização: ", ("Selecione", "Represa do Iraí", "Represa do Passaúna", "Piraquara I", "Piraquara II", "Rio Verde"))
        # Índices/ano das imagens obtidas
        # Anos faltantes: 95 98 99 01 03 06 07 08 10 13 18
        colecao = {
        '1993':('LANDSAT/LT05/C01/T1_TOA/LT05_220078_19930715'),
        '1994':('LANDSAT/LT05/C01/T1_TOA/LT05_220078_19940718'),
        '1996':('LANDSAT/LT05/C01/T1_TOA/LT05_220078_19960418'),
        '1997':('LANDSAT/LT05/C01/T1_TOA/LT05_220078_19970624'),
        '2000':('LANDSAT/LE07/C01/T1_RT_TOA/LE07_220078_20000507'),
        '2002':('LANDSAT/LE07/C01/T1_RT_TOA/LE07_220078_20020902'),
        '2004':('LANDSAT/LT05/C01/T1_TOA/LT05_220078_20040830'),
        '2015':('LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20150829'),
        '2017':('LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20170514'),
        '2019':('LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20190418'),
        '2020':('LANDSAT/LE07/C01/T1_RT_TOA/LE07_221077_20200926'),
        '2021':('LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20210525'),
                }
        chaves = tuple(colecao.keys()) # transforma as chaves do dicionário em tupla
        year = st.selectbox("Selecione o ano: ", chaves)
        id_imagem = colecao[year]
        if 'LC08' in id_imagem:
                bandas = {'bands':'B5,B4,B3'}
        else:
                bandas = {'bands':'B4,B3,B2'}
        st.markdown("----")
        Map = geemap.Map(locate_control=True, add_google_map=False)

        if local == "Represa do Iraí":
            texto = "A APA Estadual do Iraí foi criada em 06/05/1996 através do DECRETO Nº 1753"
            imagem = ee.Image(colecao[year]).clip(ee_APA_iai)
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            Map.add_styled_vector(ee_APA_iai, column="NOME_60" ,palette=palette, layer_name="APA do Iraí", **vis_params_apa)
            if year in ('2000', '2002', '2004', '2015', '2017', '2019', '2020', '2021'):
                Map.add_styled_vector(ee_reserv_irai, column="nmoriginal" ,palette=palette, layer_name="Reserva Iraí", **vis_params_reserv)
            Map.centerObject(ee_APA_iai, 12)
            Map.addLayerControl()
            st.markdown(texto)


        if local == "Represa do Passaúna":
            imagem = ee.Image(colecao[year]).clip(ee_APA_passauna)
            st.image("https://site.sanepar.com.br/sites/site.sanepar.com.br/files/imagecache/800x600/memoria/passauna_primeirafase_1986.jpg", width=300, caption="1986 - Inauguração do Sistema Passaúna (1ª Etapa)\n1992 - Sistema Passaúna - Entrega da 2ª Etapa")
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            Map.add_styled_vector(ee_APA_passauna, column="NOME_60" ,palette=palette, layer_name="APA do Passaúna", **vis_params_apa)
            Map.add_styled_vector(ee_reserv_passauna, column="nmoriginal" ,palette=palette, layer_name="Reserva Passaúna", **vis_params_reserv)
            Map.centerObject(ee_reserv_passauna, 12)
            Map.addLayerControl()

        if local == "Piraquara I":
            st.markdown("1979 - Inaugurada a Barragem do Cayuguava (também conhecida como Piraquara I), a primeira grande barragem para acumulação de água no Paraná. Fonte: Sanepar")
            st.image("https://piraquara.pr.gov.br/turismo/dbimages/-dsc0138_102091_img.jpg", width=300, caption="Barragem Piraquara I. Imagem: Sanepar")
            imagem = ee.Image(colecao[year]).clip(ee_APA_piraquara)
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            Map.add_styled_vector(ee_APA_piraquara, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
            Map.add_styled_vector(ee_reserv_piraquara, column="nmoriginal" ,palette=palette, layer_name="Reserva Piraquara I", **vis_params_reserv)
            Map.centerObject(ee_reserv_piraquara, 12)
            Map.addLayerControl()

        if local == "Piraquara II":
            st.markdown("1979 - Inaugurada a Barragem do Cayuguava (também conhecida como Piraquara I), a primeira grande barragem para acumulação de água no Paraná. Fonte: Sanepar")
            st.image("https://piraquara.pr.gov.br/turismo/dbimages/barragem-piraquara-ii-(51)_102092_img.jpg", width=300, caption="Barragem Piraquara I. Imagem: Sanepar")
            imagem = ee.Image(colecao[year]).clip(ee_APA_piraquara_II)
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            Map.add_styled_vector(ee_APA_piraquara_II, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
            Map.add_styled_vector(ee_reserv_piraquara_II, column="nmoriginal" ,palette=palette, layer_name="Reserva Piraquara II", **vis_params_reserv)
            Map.centerObject(ee_reserv_piraquara_II, 12)
            Map.addLayerControl()
            
        if local == "Rio Verde":
            imagem = ee.Image(colecao[year]).clip(ee_APA_rio_verde)
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            Map.add_styled_vector(ee_APA_rio_verde, column="NOME_60" ,palette=palette, layer_name="APA do Rio Verde", **vis_params_apa)
            Map.add_styled_vector(ee_reserv_rio_verde, column="nmoriginal" ,palette=palette, layer_name="Reserva Rio Verde", **vis_params_reserv)
            Map.centerObject(ee_reserv_rio_verde, 12)
            Map.addLayerControl()
           

        if local == "Selecione":
            Map = geemap.Map(locate_control=True, add_google_map=False)
            Map.add_styled_vector(ee_area_estudo, column="id" ,palette=palette, layer_name="Area de estudo", **vis_params_apa)
            imagem = ee.Image(colecao[year]).clip(ee_area_estudo)
            Map.addLayer(imagem, bandas, 'Imagem Landsat')
            # Map.add_styled_vector(ee_bairros, column="NOME" ,palette=palette, layer_name="Bairros Curitiba", **vis_params_apa)
            Map.addLayerControl()
            Map.centerObject(ee_area_estudo, 10)

    with col12:
        folium_static(Map)
        with st.expander("Visualizar ID da imagem:"):
            st.markdown(id_imagem)

    return
