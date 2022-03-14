import streamlit as st
import geemap.foliumap as geemap
import folium
import json
import ee
from datetime import datetime
from apps.old.dam import folium_static
from apps.satelites import copernicus, landsat


def parametros():
    """
    Esta função carrega os parâmetros para realizar as operações futuras com as imagens, o usuário interage através da aplicação
    e retorna uma imagem da coleção desejada.
    """
    colA, colB = st.columns([1,2]) 
    with colA:
        Map = geemap.Map(locate_control=True,
            add_google_map=False,
            basemap='SATELLITE',
            plugin_Draw=True,
            draw_export=True)
        keyword = st.text_input("Digite o nome do local:", "")
        if keyword:
            locations = geemap.geocode(keyword)
            if locations is not None and len(locations) > 0:
                str_locations = [str(g)[1:-1] for g in locations]
                location = st.selectbox("Selecione o local desejado:", str_locations)
                loc_index = str_locations.index(location)
                selected_loc = locations[loc_index]
                lat, lon = selected_loc.lat, selected_loc.lng
                folium.Marker(location=[lat,lon],
                 popup=location,
                 icon=folium.Icon(color='red', 
                 icon='info-sign')).add_to(Map)
                Map.set_center(lon, lat, zoom=11)
        uploaded_file = st.file_uploader("Faça upload do arquivo com a área desejada:", 
        type='GEOJSON', 
        accept_multiple_files=False)
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            a= bytes_data
            decoder = json.loads(a.decode('utf-8'))
            coord = decoder['features'][0]['geometry']['coordinates']
            geometry = ee.Geometry.Polygon(coord)
            Map.addLayer(geometry, name='Área de estudo')
            Map.center_object(geometry)
            colecoes = {
            'Selecione' : '',
            'LANDSAT': 'LANDSAT/LC08/C01/T1_TOA',
            'MODIS': 'MODIS/006/MOD09GQ',                   
            'SENTINEL': 'COPERNICUS/S2_SR'                  
            }
            satelite = st.selectbox('Selecione o Satélite: ', colecoes.keys())
            bandas_combination = {
                            'Selecione': '',
                            'Cor Natural': 'B4,B3,B2',
                            'Terra/Água': 'B5,B6,B4',
                            'Natural com Atmosfera removida': 'B7,B5,B3',
                            'Agricultura': 'B6,B5,B2',
                            'Saúde Vegetal': 'B5,B6,B2',
                            'Análise de Vegetação': 'B6,B5,B4',
                            'Infravermelho (vegetação)': 'B5,B4,B3',
                            'Falsa Cor (Urbano)': 'B7,B6,B4',                                                        
                            'Penetração atmosférica': 'B7,B6,B5',                    
                            'Infravermelho Curto': 'B7,B5,B4',                            
                            }
            if satelite != 'Selecione':
                combination = st.selectbox('Selecione a combinação de bandas: ', bandas_combination.keys())
                bands = {'bands': bandas_combination[combination]}
                if combination != 'Selecione':
                    today = str(datetime.today().strftime('%Y-%m-%d'))
                    date_start = str(st.date_input('Selecione a data (inicial): '))
                    if date_start != today:
                        date_end = str(st.date_input('Selecione a data (final): '))
                        date_range = (date_start, date_end)
                        if satelite == 'LANDSAT':
                            length, dates, ids = landsat(geometry, date_range, )
                            st.write('Quantidade de Imagens disponíveis: ', length)
                            date = st.selectbox('Datas disponíveis:', dates)
                            if date != 'Selecione':
                                    select = st.selectbox('Selecione o ID da imagem para carregar no mapa', ['Selecione'] + ids)    
                                    image = ee.Image(select)
                                    if select != 'Selecione':
                                        Map.addLayer(image, bands, name=select)
                                        Map.addLayerControl()
                


    with colB:
        folium_static(Map, width=800, height=600)
        texto = """<p  style='text-align: justify; color: #31333F;'>
                        Informações do Landsat 8:\n</p>
                        <p  style='text-align: justify; color: #31333F;'>  
                        <b>- </b>Lançamento: 11 de fevereiro de 2013;\n</p>
                        <p  style='text-align: justify; color: #31333F;'> 
                        <b>- </b>Status: Operacional;\n</p>
                        <p  style='text-align: justify; color: #31333F;'>
                        <b>- </b>Sensores: OLI, TIRS;\n</p>
                        <p  style='text-align: justify; color: #31333F;'>
                        <b>- </b>Altitude: 705 km;\n</p>
                        <p  style='text-align: justify; color: #31333F;'>
                        <b>- </b>Inclinação: 98,2°;\n</p>
                        <p  style='text-align: justify; color: #31333F;'>
                        <b>- </b>Tempo de revisita: 16 dias.</p>           
                """
        with st.expander("Visualizar dados do satélite:"):
            st.markdown(texto, unsafe_allow_html=True)
    return 