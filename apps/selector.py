from asyncio.windows_events import NULL
import streamlit as st
import geemap.foliumap as geemap
import folium
import json
import ee
from datetime import datetime
from apps.old.dam import folium_static
from apps.satelites import image_filter, landsat8
from numpy import cos, sin, tan, pi


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
    basemap='ROADMAP',
    plugin_Draw=True,
    draw_export=True,
    zoom=3,
    center=[-18.1459,-57.3047])
    # Latitude: -18.1459
    # Longitude: -57.3047
    Map.addLayerControl()
    layers = [] # Iniciando a variável que é preenchida após realizar as operações de detecção

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
    <p  style='text-align: justify; color: #31333F;'>
                        <b> ... </b>Siga os passos a esquerda.\n</p>
    """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Faça upload do arquivo com a área desejada:", 
        type='GEOJSON', 
        accept_multiple_files=False)

    colA2, colB2 = st.columns([1,2])
    with colA2:
        if marcador is not None:
            marcador.add_to(Map)
            Map.set_center(lon, lat, zoom=13)
        
           

        if uploaded_file is not None:
            st.markdown("""
            <p  style='text-align: justify; color: #3CB371;'>
            ✔️ Área carregada com sucesso
            </p>
            """, unsafe_allow_html=True)
            bytes_data = uploaded_file.read()
            a = bytes_data
            decoder = json.loads(a.decode('utf-8'))
            coord = decoder['features'][0]['geometry']['coordinates']
            geometria = ee.Geometry.Polygon(coord)
            # Map.addLayer(geometry, name='Área de interesse')
            # Map.center_object(geometry)
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
                length, dates, lis_ids = landsat8(geometria, date_range)
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
                # Detecção de mudanças NDVI
                Pnir0 = ee.Image(img0).select('B5')
                red0 = ee.Image(img0).select('B2')
                Pnir1 = ee.Image(img1).select('B5')
                red1 = ee.Image(img1).select('B2')
                NDVI_0 = (Pnir0.subtract(red0)).divide(Pnir0.add(red0))
                NDVI_1 = (Pnir1.subtract(red1)).divide(Pnir1.add(red1))
                NDVI_detect = (NDVI_1.subtract(NDVI_0))

                # Detecção de mudanças NDWI
                green0 = ee.Image(img0).select('B3')
                green1 = ee.Image(img1).select('B3')
                NDWI_0 = (green0.subtract(Pnir0)).divide(green0.add(Pnir0))
                NDWI_1 = (green1.subtract(Pnir1)).divide(green1.add(Pnir1))
                NDWI_detect = (NDWI_1.subtract(NDWI_0))

                # Detecção de mudanças RCEN

                # Import a Landsat 8 TOA image for this region.
                # var img1 = ee.Image('LANDSAT/LC08/C02/T1_RT/LC08_220067_20130706').select('B5'); Pnir já aberto
                # var img2 = ee.Image('LANDSAT/LC08/C02/T1_RT/LC08_220067_20210914').select('B5'); Pnir já aberto
                # Create a new image that is the concatenation of three images: a constant,
                # the SWIR1 band, and the SWIR2 band.
                constant = ee.Image(1)
                xVar = Pnir0
                yVar = Pnir1
                imgRegress = ee.Image.cat(constant, xVar, yVar)

                # Calculate regression coefficients for the set of pixels intersecting the
                # above defined region using reduceRegion. The numX parameter is set as 2
                # because the constant and the SWIR1 bands are independent variables and they
                # are the first two bands in the stack; numY is set as 1 because there is only
                # one dependent variable (SWIR2) and it follows as band three in the stack.

                linearRegression = imgRegress.reduceRegion(
                    reducer= ee.Reducer.linearRegression(2, 1),
                    geometry = geometria,
                    scale = 30)

                # Convert the coefficients array to a list.
                coefList = ee.Array(linearRegression.get('coefficients')).toList()

                # Extract the y-intercept and slope.
                b0 = ee.List(coefList.get(0)).get(0); # y-intercept
                b1 = ee.List(coefList.get(1)).get(0); # slope

                # Extract the residuals.
                residuals = ee.Array(linearRegression.get('residuals')).toList().get(0)

                # Inspect the results.
                # print('OLS estimates', linearRegression)
                # print('y-intercept:', b0)
                # print(linearRegression)
                # print('Residuals:', residuals)
                # print('teta: ',teta)
                teta = 0.8272143413892454
                m = tan(teta * (pi/180))
                id1 = Pnir0
                id2 = Pnir1
                p1 = id2.multiply(cos(teta))
                p2 = id1.multiply(sin(teta))
                RCEN_detect = p1.subtract(p2)


                # Abrindo comninação de bandas das imagens
                nat_0 = ee.Image(img0)
                nat_1 = ee.Image(img1)
                
                layers = st.multiselect('Selecione as camadas para carregar no mapa:', ('Área de interesse', 'Cor Natural', 'DM - Vegetação', 'DM - Água', 'DM - Urbano', "Massas d'água"))
                

    with colB2:
        if uploaded_file is not None:
            Map = geemap.Map(locate_control=True,
            add_google_map=False,
            basemap='ROADMAP',
            plugin_Draw=True,
            draw_export=True)
            Map.centerObject(geometria)
            # if 'Mapa Base Satélite' in layers:
            #     Map.add_basemap('SATELLITE')

            if 'Cor Natural' in layers:
                Map.addLayer(nat_0, {'bands': 'B7,B5,B3'}, name= 'Cor Natural - ' + dates[0])
                Map.addLayer(nat_1, {'bands': 'B7,B5,B3'}, name= 'Cor Natural - ' + dates[1])
               
            if 'DM - Vegetação' in layers:
                Map.addLayer(NDVI_detect, name= 'DM - NDVI')

            if 'DM - Água' in layers:
                Map.addLayer(NDWI_detect, name= 'DM - NDWI')

            if 'DM - Urbano' in layers:
                Map.addLayer(RCEN_detect, name= 'DM - RCEN')

            if 'Área de interesse' in layers:
                vis_params_area = {
                        'color': '#FFA500', 
                        'pointSize': 3,
                        'pointShape': 'circle',
                        'width': 2,
                        'lineType': 'dotted',
                        'fillColor': '00000000',}
                area_interesse = ee.FeatureCollection(geometria)
                Map.addLayer(area_interesse.style(**vis_params_area), {}, 'Área de interesse')
                
            if "Massas d'água" in layers:
                massa_dagua = ee.FeatureCollection("projects/projetofinal-340114/assets/Massa_dagua") # Adicionar shp de diretorio do gee
                vis_params = {
                        'color': '#4169E1', 
                        'pointSize': 3,
                        'pointShape': 'circle',
                        'width': 2,
                        'lineType': 'dotted',
                        'fillColor': '00000000',}
                Map.addLayer(massa_dagua.style(**vis_params), {}, "Massas d'água")
            



        Map.addLayerControl()
        folium_static(Map, width=800, height=600)
        texto = """<h6  style='text-align: justify; color: #31333F;'>
                        Informações sobre o Satélite:\n</h6>
                        <p  style='text-align: justify; color: #31333F;'>  
                        <b>- </b>Satélite: Landsat 8\n</p>
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
        with st.expander("Informação sobre os dados do mapa:"):
            st.markdown(texto, unsafe_allow_html=True)
        st.markdown("""
        <p  style='text-align: justify; color: #31333F;'>
        🔲 Regiões com tom mais claro são áreas onde <b>houve</b> mudança.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("""
        <p  style='text-align: justify; color: #31333F;'>
        🔳 Regiões com tom mais escuro são áreas onde <b>não houve</b> mudança.
        </p>
        """, unsafe_allow_html=True)
    return 