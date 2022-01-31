from asyncio.windows_events import NULL
import streamlit.components.v1 as components
import streamlit as st
import geemap.foliumap as geemap
import folium

def folium_static(fig, width=700, height=500):
    if isinstance(fig, folium.Map):
        fig = folium.Figure().add_child(fig)
    return components.html(fig.render(), height=(fig.height or height) + 10, width=width)


def orbital(titulo):
    st.title(titulo)
    st.markdown("----")
    st.markdown("Abaixo pode ser digitado um endereço ou o nome de uma localidade para ir com o mapa até a área de interesse:")
    row1_col1, row1_col2 = st.columns([2, 1])
    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4
    m = geemap.Map(
    plugin_Draw=True,
    draw_export=True,
    locate_control=True,
    plugin_LatLngPopup=False,)
    m.setCenter(-49.232055346903806, -25.448467407922067, 17)
    m.add_basemap("SATELLITE")
    # m.split_map(left_layer='HYBRID', right_layer='ESRI')
    # m.add_landsat_ts_gif(label='Place name', start_year=1985, bands=['NIR', 'Red', 'Green'], frames_per_second=5)
    m.addLayerControl()
    with row1_col2:
        keyword = st.text_input("Digite a localização:", "")
        if keyword:
            locations = geemap.geocode(keyword)
            if locations is not None and len(locations) > 0:
                str_locations = [str(g)[1:-1] for g in locations]
                location = st.selectbox("Select a location:", str_locations)
                loc_index = str_locations.index(location)
                selected_loc = locations[loc_index]
                lat, lng = selected_loc.lat, selected_loc.lng
                folium.Marker(location=[lat, lng], popup=location).add_to(m)
                m.set_center(lng, lat, 17)
        st.markdown("Marque a área desejada e exporte o arquivo 'Geojson'")
        collection = ["Landsat TM-ETM-OLI Surface Reflectance"]
        uploaded_file = st.file_uploader("Selecione o Geojson: ", type=["geojson"], accept_multiple_files=False)
        arquivo = uploaded_file
        if arquivo is not None:
            ee_object = geemap.geojson_to_ee(arquivo)
            m.addLayer(ee_object,'Área de interesse')

    if keyword is not None:
        with row1_col1:
            folium_static(m, width=550)
            # m.to_streamlit(height=600)
    return


