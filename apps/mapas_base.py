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
    ee.Initialize()
    st.title(titulo)
    st.markdown("----")
    st.markdown("Nesta seção é possível encontrar uma análise temporal dos reservatórios da região de Curitiba.")
    row1_col1, row1_col2 = st.columns([2, 1])
    # m = geemap.Map(
    # plugin_Draw=True,
    # draw_export=True,
    # locate_control=True,
    # plugin_LatLngPopup=False,)
    # m.setCenter(-49.232055346903806, -25.448467407922067, 17)
    # # m.split_map(left_layer='HYBRID', right_layer='ESRI')
    # # m.add_landsat_ts_gif(label='Place name', start_year=1985, bands=['NIR', 'Red', 'Green'], frames_per_second=5)
    # m.addLayerControl()
    with row1_col2:
        local = st.selectbox("Selecione o local para visualização: ", ("Represa do Iraí", "Represa do Passaúna", "Piraquara I", "Piraquara II"))
        if local == "Represa do Iraí":
            geojson_file_path = "./data/irai.geojson"
            ee_object = geemap.geojson_to_ee(geojson_file_path)
            Map = geemap.Map(locate_control=True)
            Map.addLayer(ee_object, {}, 'Represa iraí')
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


