import matplotlib.pyplot as plt
import streamlit as st
import geemap.foliumap as geemap
import ee
from apps.dam import folium_static


def region():
    # Estilo da camada area NUC
    style_area_nuc = {'color': '#B22222', 'colorOpacity': 0.5, 'width': 4, 'lineType': 'dotted'}
    # Estilo da camada da NUC
    rm = '#FDF5E6'
    rg = '#BC8F8F'
    style_NUC = {"Almirante Tamandaré": rm, "Araucária":rm, "Campina Grande do Sul": rm, "Campo Largo":  rm, "Campo Magro": rm,
                "Colombo": rm, "Fazenda Rio Grande": rm, "Itaperuçu": rm, "Pinhais": rm, "Piraquara": rm, "Quatro Barras": rm, 
                "Rio Branco do Sul": rm, "São José dos Pinhais": rm, "Curitiba": rg}
    # Carregando geojson
    path_a = "./data/base/NUC_A.geojson"
    ee_NUC_a = geemap.geojson_to_ee(path_a)
    path_n = "./data/base/NUC_N.geojson"
    ee_NUC = geemap.geojson_to_ee(path_n)
    Map = geemap.Map(locate_control=True, add_google_map=False)
    Map.add_basemap('CartoDB.VoyagerNoLabels')
    Map.setCenter(-49.2732, -25.4453, zoom = 9)
    Map.add_styled_vector(ee_NUC, column="NM_MUN", palette=style_NUC, layer_name="Municípios do NUC")
    Map.addLayer(ee_NUC_a, vis_params=style_area_nuc, name="NUC")
    Map.add_labels(ee_NUC, column="NM_MUN", font_size= "8pt", font_color="#1C1C1C", layer_name='Rótulos', font_weight="bold")
    Map.addLayerControl()
    folium_static(Map, width=1200, height=600)  
    return 
