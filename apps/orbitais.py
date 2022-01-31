import streamlit.components.v1 as components
import streamlit as st
import geemap.foliumap as geemap
import folium

def folium_static(fig, width=700, height=500):
    if isinstance(fig, folium.Map):
        fig = folium.Figure().add_child(fig)

    return components.html(
        fig.render(), height=(fig.height or height) + 10, width=width
    )

def orbital(titulo):
    st.title(titulo)
    st.markdown("----")
    row1_col1, row1_col2 = st.columns([2, 1])
    if st.session_state.get("zoom_level") is None:
        st.session_state["zoom_level"] = 4

    with row1_col1:
        m = geemap.Map(basemap="HYBRID",
        plugin_Draw=True,
        draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,)
        m.add_basemap("ROADMAP")

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
                st.session_state["zoom_level"] = 12
    if keyword is not None:
        with row1_col1:
            folium_static(m, width=550)

    return