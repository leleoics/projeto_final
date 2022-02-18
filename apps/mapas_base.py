import streamlit.components.v1 as components
import streamlit as st
import geemap.foliumap as geemap
import folium
import ee


def folium_static(fig, width=800, height=650):
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
    vis_params_apa = {'color': '#228B22', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 2, 'lineType': 'solid', 'fillColorOpacity': 0.1}
    # Parâmetros de estilo para o reservatório
    vis_params_reserv = {'color': '#9cc0f9', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 1, 'lineType': 'solid', 'fillColorOpacity': 0.15}
    # Paleta de cores em comum 
    palette = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    # Carregando dados e convertendo para objetos ee
    geojson_area_estudo = "./data/area_estudo.geojson"
    ee_area_estudo = geemap.geojson_to_ee(geojson_area_estudo)
    #                       Irai
    geojson_reserv_irai = "./data/reserv_irai.geojson"
    geojson_APA_irai = "./data/APA_irai.geojson"
    ee_APA_iai = geemap.geojson_to_ee(geojson_APA_irai)
    ee_reserv_irai = geemap.geojson_to_ee(geojson_reserv_irai)

    #                     Passauna
    geojson_reserv_passauna = "./data/reserv_passauna.geojson"
    geojson_APA_passauna = "./data/APA_passauna.geojson"
    ee_APA_passauna = geemap.geojson_to_ee(geojson_APA_passauna)
    ee_reserv_passauna = geemap.geojson_to_ee(geojson_reserv_passauna)


    #                     Piraquara I
    geojson_reserv_piraquaraI = "./data/reserv_piraquara_I.geojson"
    geojson_APA_piraquara = "./data/APA_piraquara.geojson"
    ee_APA_piraquara = geemap.geojson_to_ee(geojson_APA_piraquara)
    ee_reserv_piraquara = geemap.geojson_to_ee(geojson_reserv_piraquaraI)


    #                     Piraquara II
    geojson_reserv_piraquaraII = "./data/reserv_piraquara_II.geojson"
    geojson_APA_piraquara = "./data/APA_piraquara.geojson"
    ee_APA_piraquara_II = geemap.geojson_to_ee(geojson_APA_piraquara)
    ee_reserv_piraquara_II = geemap.geojson_to_ee(geojson_reserv_piraquaraII)

    
    #                      Rio Verde
    geojson_reserv_rioverde = "./data/reserv_rio_verde.geojson"
    geojson_APA_rioverde = "./data/APA_rio_verde.geojson"
    ee_APA_rio_verde = geemap.geojson_to_ee(geojson_APA_rioverde)
    ee_reserv_rio_verde = geemap.geojson_to_ee(geojson_reserv_rioverde)

    row1_col1, row1_col2 = st.columns([2, 1])
    with row1_col2:
        local = st.selectbox("Selecione o local para visualização: ", ("Represa do Iraí", "Represa do Passaúna", "Piraquara I", "Piraquara II", "Rio Verde"))
        # Índices/ano das imagens obtidas
# Anos faltantes: 95 98 99 01 03 06 07 08 10 13 18
        colecao = {
        '1993':'LANDSAT/LT05/C01/T1_TOA/LT05_220078_19930715',
        '1994':'LANDSAT/LT05/C01/T1_TOA/LT05_220078_19940718',
        '1996':'LANDSAT/LT05/C01/T1_TOA/LT05_220078_19960418',
        '1997':'LANDSAT/LT05/C01/T1_TOA/LT05_220078_19970624',
        '2000':'LANDSAT/LE07/C01/T1_RT_TOA/LE07_220078_20000507',
        '2002':'LANDSAT/LE07/C01/T1_RT_TOA/LE07_220078_20020902',
        '2004':'LANDSAT/LT05/C01/T1_TOA/LT05_220078_20040830',
        '2015':'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20150829',
        '2017':'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20170514',
        '2019':'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20190418',
        '2020':'LANDSAT/LE07/C01/T1_RT_TOA/LE07_221077_20200926',
        '2021':'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20210525',
                }
        chaves = tuple(colecao.keys()) # transforma as chaves do dicionário em tupla

        if local != 'Selecione':
            year = st.selectbox("Selecione o ano: ", chaves)
            id_imagem = colecao[year]
            if 'LC08' in id_imagem:
                    bandas = {'bands':'B6,B5,B4'}
            else:
                    bandas = {'bands':'B5,B4,B3'}

            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("----")
            st.markdown("Visualizando a coleção:\n{}".format(colecao[year]))
            Map = geemap.Map(locate_control=True, add_google_map=False)
            if local == "Represa do Iraí":
                # Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(colecao[year]).clip(ee_APA_iai)
                Map.addLayer(imagem, bandas, 'Landsat 8')
                Map.add_styled_vector(ee_APA_iai, column="NOME_60" ,palette=palette, layer_name="APA do Iraí", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_irai, column="nmoriginal" ,palette=palette, layer_name="Reserva Iraí", **vis_params_reserv)
                Map.centerObject(ee_APA_iai, 12)
                Map.addLayerControl()

            if local == "Represa do Passaúna":
                # Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(colecao[year]).clip(ee_APA_passauna)
                Map.addLayer(imagem, bandas, 'Landsat 8')
                Map.add_styled_vector(ee_APA_passauna, column="NOME_60" ,palette=palette, layer_name="APA do Passaúna", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_passauna, column="nmoriginal" ,palette=palette, layer_name="Reserva Passaúna", **vis_params_reserv)
                Map.centerObject(ee_reserv_passauna, 12)
                Map.addLayerControl()

            if local == "Piraquara I":
                # Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(colecao[year]).clip(ee_APA_piraquara)
                Map.addLayer(imagem, bandas, 'Landsat 8')
                Map.add_styled_vector(ee_APA_piraquara, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_piraquara, column="nmoriginal" ,palette=palette, layer_name="Reserva Piraquara I", **vis_params_reserv)
                Map.centerObject(ee_reserv_piraquara, 12)
                Map.addLayerControl()

            if local == "Piraquara II":
                # Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(colecao[year]).clip(ee_APA_piraquara_II)
                Map.addLayer(imagem, bandas, 'Landsat 8')
                Map.add_styled_vector(ee_APA_piraquara_II, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_piraquara_II, column="nmoriginal" ,palette=palette, layer_name="Reserva Piraquara II", **vis_params_reserv)
                Map.centerObject(ee_reserv_piraquara_II, 12)
                Map.addLayerControl()
                
            if local == "Rio Verde":
                # Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(colecao[year]).clip(ee_APA_rio_verde)
                Map.addLayer(imagem, bandas, 'Landsat 8')
                Map.add_styled_vector(ee_APA_rio_verde, column="NOME_60" ,palette=palette, layer_name="APA do Rio Verde", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_rio_verde, column="nmoriginal" ,palette=palette, layer_name="Reserva Rio Verde", **vis_params_reserv)
                Map.centerObject(ee_reserv_rio_verde, 12)
                Map.addLayerControl()
           

        else:
            Map = geemap.Map(locate_control=True, add_google_map=False)
            Map.add_styled_vector(ee_area_estudo, column="id" ,palette=palette, layer_name="Area de estudo", **vis_params_apa)
            imagem = ee.Image(colecao[year]).clip(ee_area_estudo)
            Map.addLayer(imagem, bandas, 'Landsat 8')
            Map.centerObject(ee_area_estudo, 10)

    with row1_col1:
        folium_static(Map, width=550)


    return
