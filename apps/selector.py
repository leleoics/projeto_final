import streamlit as st
import geemap.foliumap as geemap
import folium
import json
import ee
from datetime import datetime
from apps.old.dam import folium_static
from apps.satelites import image_filter, landsat8



def geolocator(keyword):
    """
    Esta função retorna um marcador para a aplicação.
    """
    if keyword:
        locations = geemap.geocode(keyword)
        if locations is not None and len(locations) > 0:
            str_locations = [str(g)[1:-1] for g in locations]
            location = st.selectbox("Selecione o local desejado:", str_locations)
            loc_index = str_locations.index(location)
            selected_loc = locations[loc_index]
            lat, lon = selected_loc.lat, selected_loc.lng
            marker = folium.Marker(location=[lat,lon],
                popup=location,
                icon=folium.Icon(color='red', 
                icon='info-sign'))
            if marker is not None:
                return marker, lon, lat


def parametros():
    """
    Esta função carrega os parâmetros para realizar as operações futuras com as imagens, o usuário interage através da aplicação
    e retorna uma imagem da coleção desejada.
    """
    Map = geemap.Map(locate_control=True,
    add_google_map=False,
    basemap='SATELLITE',
    plugin_Draw=True,
    draw_export=True)
    Map.addLayerControl()


    colA1, colB1 = st.columns([1,1]) 
    with colA1:
        st.markdown("""
    <p  style='text-align: justify; color: #31333F;'>
                        Esta ferramenta permite que seja realizado a detecção de mudanças em uma área de interesse do usuário:\n</p>
    <p  style='text-align: justify; color: #31333F;'>
                        Para isso, siga o passo a passo ao lado <b> -> </b>\n</p>
    <p  style='text-align: justify; color: #31333F;'>
                         </b>\n</p>
    """, unsafe_allow_html=True)
        chave = st.text_input("Digite o nome do local:", "")
        marcador = None
        if chave:
            marcador, lon, lat = geolocator(chave)


    with colB1:
        st.markdown("""
    <p  style='text-align: justify; color: #31333F;'>
                        <b> 1 - </b>Digite a localizaçao para centralizar o mapa:\n</p>
    <p  style='text-align: justify; color: #31333F;'>
                        <b> 2 - </b>Desenhe a área de interesse no mapa:\n</p>
    <p  style='text-align: justify; color: #31333F;'>
                        <b> 3 - </b>Exporte a área de interesse                 :\n</p>
    <p  style='text-align: justify; color: #31333F;'>
                        <b> 4 - </b>Faça o Upload do arquivo Geojson gerado     :\n</p>
    """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Faça upload do arquivo com a área desejada:", 
        type='GEOJSON', 
        accept_multiple_files=False)

    colA2, colB2 = st.columns([1,2])
    with colA2:
        Map = geemap.Map(locate_control=True,
             add_google_map=False,
             basemap='ROADMAP',
             plugin_Draw=True,
             draw_export=True)
        Map.addLayerControl()
        if marcador is not None:
            marcador.add_to(Map)
            Map.set_center(lon, lat, zoom=11)
        # mun = ee.FeatureCollection("projects/projetofinal-340114/assets/BR_UF_2021")
        # Map.addLayer(mun, name='Estados do Brasil')
        # Map.addLayerControl()
        # keyword = st.text_input("Digite o nome do local:", "")
        # if keyword:
        #     locations = geemap.geocode(keyword)
        #     if locations is not None and len(locations) > 0:
        #         str_locations = [str(g)[1:-1] for g in locations]
        #         location = st.selectbox("Selecione o local desejado:", str_locations)
        #         loc_index = str_locations.index(location)
        #         selected_loc = locations[loc_index]
        #         lat, lon = selected_loc.lat, selected_loc.lng
        #         folium.Marker(location=[lat,lon],
        #          popup=location,
        #          icon=folium.Icon(color='red', 
        #          icon='info-sign')).add_to(Map)
        #         Map.set_center(lon, lat, zoom=11)
        # uploaded_file = st.file_uploader("Faça upload do arquivo com a área desejada:", 
        # type='GEOJSON', 
        # accept_multiple_files=False)
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            a= bytes_data
            decoder = json.loads(a.decode('utf-8'))
            coord = decoder['features'][0]['geometry']['coordinates']
            geometry = ee.Geometry.Polygon(coord)
            # Map.addLayer(geometry, name='Área de interesse')
            # Map.center_object(geometry)
                 

            # satelite = st.multiselect('Selecione o Satélite: ', colecoes.keys())
            # bandas_combination = {
            #                 'Selecione': '',
            #                 'Cor Natural': 'B4,B3,B2',
            #                 'Terra/Água': 'B5,B6,B4',
            #                 'Natural com Atmosfera removida': 'B7,B5,B3',
            #                 'Agricultura': 'B6,B5,B2',
            #                 'Saúde Vegetal': 'B5,B6,B2',
            #                 'Análise de Vegetação': 'B6,B5,B4',
            #                 'Infravermelho (vegetação)': 'B5,B4,B3',
            #                 'Falsa Cor (Urbano)': 'B7,B6,B4',                                                        
            #                 'Penetração atmosférica': 'B7,B6,B5',                    
            #                 'Infravermelho Curto': 'B7,B5,B4',                            
            #                 }

            today = str(datetime.today().strftime('%Y-%m-%d'))
            date_start = str(st.date_input('Selecione a data (inicial): '))
            if date_start != today:
                date_end = str(st.date_input('Selecione a data (final): '))
                date_range = (date_start, date_end)
                length, dates, lis_ids = landsat8(geometry, date_range)
                st.write('Quantidade de Imagens disponíveis nesse período: ', length)
                st.markdown("""
                <p  style='text-align: justify; color: #31333F;'>
                    O satélite faz a revisita a cada 16 dias e existe uma filtragem de núvens, portanto a depender do período definido,
                     pode ser encontrado uma baixa quantidade de imagens. As datas de imagens com visibilidade na região mais próximas 
                     do período definido são:\n</p>
                <p  style='text-align: justify; color: #31333F;'>""", unsafe_allow_html=True)
                st.markdown('- ' + dates[0])
                st.markdown('- ' + dates[1])
                # st.write(lis_ids) # Colocar em ver mais
                Imgs = image_filter(dates, lis_ids)
                img0 = Imgs[0]
                img1 = Imgs[1]   
                Pnir0 = ee.Image(img0).select('B5')
                red0 = ee.Image(img0).select('B2')
                Pnir1 = ee.Image(img1).select('B5')
                red1 = ee.Image(img1).select('B2')
                # Map.addLayer(Pnir0, name= 'Infravermelho Próximo - ' + dates[0])
                # Map.addLayer(red0, name='Vermelho - ' + dates[0])
                # Map.addLayer(Pnir1, name= 'Infravermelho Próximo - ' + dates[1])
                # Map.addLayer(red1, name='Vermelho - ' + dates[1])
                NDVI_0 = (Pnir0.subtract(red0)).divide(Pnir0.add(red0))
                NDVI_1 = (Pnir1.subtract(red1)).divide(Pnir1.add(red1))
                NDVI_detect = (NDVI_1.subtract(NDVI_0))
                Map.addLayer(NDVI_0, name= 'NDVI - ' + dates[0])
                Map.addLayer(NDVI_1, name= 'NDVI - ' + dates[1])
                Map.addLayer(NDVI_detect, name= 'Detecção de mudanças - ' + dates[1])


                # dataset, visualization =  landsat8(geometry, date_range)
                # Map.addLayer(dataset, visualization, name = 'Coleção Landsat 08')
                # Map.addLayer(geometry, name='Área importada')
                # Map.addLayerControl()    

                        # if 'LANDSAT 09' in satelite:
                        #     dataset, visualization =  landsat9(geometry, date_range)
                        #     Map.addLayer(dataset, visualization, name = 'Coleção Landsat 09')
                        #     Map.addLayer(geometry, name='Área importada')
                            

                        # if 'SENTINEL' in satelite:
                        #     dataset, visualization =  copernicus(geometry, date_range)
                        #     Map.addLayer(dataset, visualization, name = 'Coleção Copernicus')


                        # if 'NDVI' in satelite:
                        #     dataset, visualization =  ndvi(date_range)
                        #     Map.addLayer(dataset, visualization, name = 'NDVI')

                        


    with colB2:
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