import matplotlib.pyplot as plt
import streamlit as st
import geemap.foliumap as geemap
import folium
import ee
from apps.dam import folium_static


def growth(titulo):
    st.title(titulo)
    # Carregando geojson
    # style_NUC = {'color': '#9cc0f9', 'colorOpacity': 1, 'pointSize': 3, 'pointShape': 'circle', 'width': 1, 'lineType': 'solid', 'fillColorOpacity': 0.15}
    geojson_NUC = "./data/base/NUC_N.geojson"
    ee_NUC = geemap.geojson_to_ee(geojson_NUC)
    Map = geemap.Map(locate_control=True, add_google_map=False)
    Map.setCenter(-49.2732, -25.4453, zoom = 9)
    Map.addLayer(ee_NUC, "Núcleo Urbano Central",)
    Map.add_labels(ee_NUC, column="NM_MUN", font_size= "8pt", font_color="green")
    Map.addLayerControl()
    folium_static(Map)   
    

    return

