import streamlit as st
import geemap.foliumap as geemap
import folium
import json
import ee
from datetime import datetime
from apps.dam import folium_static


def remove_duplicates_list(x):
  return list(dict.fromkeys(x))


def params_classify():
    params = dict()
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
            'LANDSAT 08':'LANDSAT/LC08/C01/T1_TOA',
            'LANDSAT 05': 'LANDSAT/LT05/C01/T1_TOA',                   
            }
            satellite = st.selectbox('Selecione o Satélite: ', colecoes.keys())
            if satellite == 'LANDSAT 08':
                        bandas_combination = {
                            'Cor Natural': 'B4,B3,B2',
                            'Falsa Cor (Urbano)': 'B7,B6,B4',
                            'Infravermelho (vegetação)': 'B5,B4,B3',
                            'Agricultura': 'B6,B5,B2',
                            'Penetração atmosférica': 'B7,B6,B5',
                            'Saúde Vegetal': 'B5,B6,B2',
                            'Terra/Água': 'B5,B6,B4',
                            'Saúde Vegetal': 'B5,B6,B2',
                            'Natural com Atmosfera removida': 'B7,B5,B3',
                            'Infravermelho Curto': 'B7,B5,B4',
                            'Análise de Vegetação': 'B6,B5,B4',
                            }
            if satellite == 'LANDSAT 05':
                        bandas_combination = {
                            'Cor Natural': 'B4,B3,B2',
                            'Falsa Cor (Urbano)': 'B7,B6,B4',
                            'Infravermelho (vegetação)': 'B5,B4,B3',
                            'Agricultura': 'B6,B5,B2',
                            'Penetração atmosférica': 'B7,B6,B5',
                            'Saúde Vegetal': 'B5,B6,B2',
                            'Terra/Água': 'B5,B6,B4',
                            'Saúde Vegetal': 'B5,B6,B2',
                            'Natural com Atmosfera removida': 'B7,B5,B3',
                            'Infravermelho Curto': 'B7,B5,B4',
                            'Análise de Vegetação': 'B6,B5,B4',
                            }
            today = str(datetime.today().strftime('%Y-%m-%d'))
            date_start = str(st.date_input('Selecione a data inicial: '))
            date_end = str(st.date_input('Selecione a data final: '))
            if date_start != today:
                date_range = (date_start, date_end)
                collection = ee.ImageCollection(colecoes[satellite]).filterMetadata('CLOUD_COVER', 'less_than', 2).filterDate(date_range[0], date_range[1]).filterBounds(geometry)
                features = collection.getInfo()
                length = len(features['features'])
                st.write('Quantidade de Imagens disponíveis: ', length)
                ids, dates = [], []
                for i in range(0, (length)):
                    name = features['features'][i]['id']
                    # date = name[-8:-4] + '-' + name[-4:-2] + '-' + name[-2:]
                    date = name[-2:] + '/' + name[-4:-2] + '/' + name[-8:-4]
                    ids.append(name)                                        
                    dates.append(date)
                dates = ['Selecione'] + remove_duplicates_list(dates)
                date = st.selectbox('Datas disponíveis:', dates)
                if date != 'Selecione':
                    date_r =  date[-4:] + date[-7:-5] + date[-10:-8]
                    select_ids = []
                    for id in ids:
                        if date_r in id:
                            select_ids.append(id)
                    select = st.selectbox('Selecione o ID da imagem para carregar no mapa', select_ids)    
                    image = ee.Image(select)
                    combination = st.selectbox('Selecione a combinação de bandas: ', bandas_combination.keys())
                    Map.addLayer(image, bandas_combination[combination], name ='Imagem orbital')
                    Map.add_layer_control()


    with colB:
        folium_static(Map, width=800, height=600)

    
    return params