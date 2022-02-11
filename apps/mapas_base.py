import streamlit.components.v1 as components
import streamlit as st
import geemap.foliumap as geemap
import folium
import ee

def folium_static(fig, width=700, height=500):
    if isinstance(fig, folium.Map):
        fig = folium.Figure().add_child(fig)
    return components.html(fig.render(), height=(fig.height or height) + 10, width=width)


def reservatorios(titulo):
    st.title(titulo)
    st.markdown("----")
    st.markdown("Nesta seção é possível encontrar uma análise temporal dos reservatórios da região de Curitiba.")
    row1_col1, row1_col2 = st.columns([2, 1])

    with row1_col2:
        local = st.selectbox("Selecione o local para visualização: ", ("Represa do Iraí", "Represa do Passaúna", "Piraquara I", "Piraquara II"))
        # colecao = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT_TOA').filterMetadata('CLOUD_COVER', 'less_than', 2)
        if local == "Represa do Iraí":
            list_colection = [  'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20150829',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20160612',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20170514',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20190418',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20200404',
                                'LANDSAT/LC08/C01/T1_RT_TOA/LC08_220078_20210525']
            # Índices/ano das imagens obtidas
            # 0 = 2015 ; 1 = 2016 ; 2 = 2017 ; 3 = 2019 ; 4 = 2020 ; 5 = 2021

            geojson_file_path = "./data/irai.geojson"
            ee_object = geemap.geojson_to_ee(geojson_file_path)
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
            st.markdown('Visualizando a coleção:\n ')
            Map = geemap.Map(locate_control=True)
            imagem = ee.Image(list_colection[id]).clip(ee_object)
            Map.addLayer(ee_object, {}, 'Represa iraí')
            Map.addLayer(imagem, {'bands':'B6,B5,B4'}, 'Landsat 8')
            Map.centerObject(ee_object, 13)
            Map.addLayerControl()

        if local == "Represa do Passaúna":
            geojson_file_path = "./data/passauna.geojson"
            ee_object = geemap.geojson_to_ee(geojson_file_path)
            Map = geemap.Map(locate_control=True)
            Map.addLayer(ee_object, {}, 'Represa do Passaúna')
            Map.centerObject(ee_object, 12)
            Map.addLayerControl()

        if local == "Piraquara I":
            geojson_file_path = "./data/piraquaraI.geojson"
            ee_object = geemap.geojson_to_ee(geojson_file_path)
            Map = geemap.Map(locate_control=True)
            Map.addLayer(ee_object, {}, 'Reservatório Piraquara I')
            Map.centerObject(ee_object, 12)
            Map.addLayerControl()

        if local == "Piraquara II":
            geojson_file_path = "./data/piraquaraII.geojson"
            ee_object = geemap.geojson_to_ee(geojson_file_path)
            Map = geemap.Map(locate_control=True)
            Map.addLayer(ee_object, {}, 'Reservatório Piraquara II')
            Map.centerObject(ee_object, 12)
            Map.addLayerControl()


    with row1_col1:
        folium_static(Map, width=550)


    return


