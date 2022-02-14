import streamlit.components.v1 as components
import streamlit as st
import geemap.foliumap as geemap
import folium
import ee


def folium_static(fig, width=800, height=650):
    if isinstance(fig, folium.Map):
        fig = folium.Figure().add_child(fig)
    return components.html(fig.render(), height=(fig.height or height), width=width)


def reservatorios(titulo):
    st.title(titulo)
    st.markdown("----")
    st.markdown("Nesta seção é possível encontrar uma análise temporal dos reservatórios da região de Curitiba.")
    row1_col1, row1_col2 = st.columns([2, 1])

    with row1_col2:
        # Carregando dados e convertendo para objetos ee
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

        local = st.selectbox("Selecione o local para visualização: ", ("Selecione", "Represa do Iraí", "Represa do Passaúna", "Piraquara I", "Piraquara II"))
        # Índices/ano das imagens obtidas
        # 0 = 2015 ; 1 = 2016 ; 2 = 2017 ; 3 = 2019 ; 4 = 2020 ; 5 = 2021
        list_colection = [  'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20150829',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20160612',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20170514',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20190418',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20200404',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20210525']
        # Parâmetros de estilo para a APA #visualizar depois com linha dotted
        vis_params_apa = {'color': '#228B22', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 2, 'lineType': 'solid', 'fillColorOpacity': 0.1}
        # Parâmetros de estilo para o reservatório
        vis_params_reserv = {'color': '#9cc0f9', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 1, 'lineType': 'solid', 'fillColorOpacity': 0.15}
        # Paleta de cores em comum 
        palette = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
        if local != 'Selecione':
            year = st.selectbox("Selecione o ano: ", ('2015', '2016', '2017', '2019', '2020', '2021'))
            if year == '2015':
                id = 0
            if year == '2016':
                id = 1
            if year == '2017':
                id = 2
            if year == '2019':
                id = 3
            if year == '2020':
                id = 4
            if year == '2021':
                id = 5
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("----")
            st.markdown("Visualizando a coleção:\n{}".format(list_colection[id]))

            if local == "Represa do Iraí":
                Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(list_colection[id]).clip(ee_APA_iai)
                Map.addLayer(imagem, {'bands':'B6,B5,B4'}, 'Landsat 8')
                Map.add_styled_vector(ee_APA_iai, column="NOME_60" ,palette=palette, layer_name="APA do Iraí", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_irai, column="nmoriginal" ,palette=palette, layer_name="Represa Iraí", **vis_params_reserv)
                Map.centerObject(ee_APA_iai, 12)
                Map.addLayerControl()

            if local == "Represa do Passaúna":
                Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(list_colection[id]).clip(ee_APA_passauna)
                Map.addLayer(imagem, {'bands':'B6,B5,B4'}, 'Landsat 8')
                Map.add_styled_vector(ee_APA_passauna, column="NOME_60" ,palette=palette, layer_name="APA do Passaúna", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_passauna, column="nmoriginal" ,palette=palette, layer_name="Represa Passaúna", **vis_params_reserv)
                Map.centerObject(ee_reserv_passauna, 12)
                Map.addLayerControl()

            if local == "Piraquara I":
                Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(list_colection[id]).clip(ee_APA_piraquara)
                Map.addLayer(imagem, {'bands':'B6,B5,B4'}, 'Landsat 8')
                Map.add_styled_vector(ee_APA_piraquara, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_piraquara, column="nmoriginal" ,palette=palette, layer_name="Represa Piraquara I", **vis_params_reserv)
                Map.centerObject(ee_reserv_piraquara, 12)
                Map.addLayerControl()

            if local == "Piraquara II":
                Map = geemap.Map(locate_control=True, add_google_map=False)
                imagem = ee.Image(list_colection[id]).clip(ee_APA_piraquara_II)
                Map.addLayer(imagem, {'bands':'B6,B5,B4'}, 'Landsat 8')
                Map.add_styled_vector(ee_APA_piraquara_II, column="NOME_60" ,palette=palette, layer_name="APA do Piraquara", **vis_params_apa)
                Map.add_styled_vector(ee_reserv_piraquara_II, column="nmoriginal" ,palette=palette, layer_name="Represa Piraquara II", **vis_params_reserv)
                Map.centerObject(ee_reserv_piraquara_II, 12)
                Map.addLayerControl()

        else:
            Map = geemap.Map(locate_control=True, add_google_map=False)
            st.markdown("obs: Carregar aqui uma visualização geral dos reservatórios")

    with row1_col1:
        folium_static(Map, width=550)


    return
