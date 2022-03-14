import streamlit as st
import geemap.foliumap as geemap
import folium
import json
import ee
from datetime import datetime
from apps.old.dam import folium_static
from numpy import mean


def maskS2clouds(image):
    """
    Entra uma coleção de imagens e realiza um filtro indicando as condições de nuvem.
    """
    qa = image.select('QA60')
    # Bits 10 e 11 são nuvens e cirrus, respectivamente.
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11
    # Se ambos sinalizarem 0 as condições da imagem são boas.
    mask = qa.bitwiseAnd(cloudBitMask).eq(0) and (qa.bitwiseAnd(cirrusBitMask).eq(0))
    return image.updateMask(mask).divide(10000)
    
def copernicus(geometry, date_range):
    """
    Esta função seleciona imagens copernicus.
    Entrada: geometry: geometria, date_range: data inicial, data final.
    Saída: dataset: coleção de imagem, visualization: parâmetros de visualização.
    """
    dataset = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(date_range[0], date_range[1]).filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20)).map(maskS2clouds).filterBounds(geometry)
    # Pre-filter to get less cloudy granules.
    visualization = {'min': 0.0,
                    'max': 0.3,
                    'bands': ['B4', 'B3', 'B2']}
    return dataset, visualization


def remove_duplicates_list(x):
    """
    Esta função retorna uma lista, com as dupliadas removidas.
    """
    return list(dict.fromkeys(x))


def landsat(geometry, date_range):
    """
    Esta função seleciona imagens Landsat.
    Entrada: geometry: geometria, date_range: data inicial, data final.
    Saída: dataset: coleção de imagem, length: quantidade de imagens, dates: data das imagens, select_ids: identificadores
    """
    dataset = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA').filterMetadata('CLOUD_COVER', 'less_than', 2).filterDate(date_range[0], date_range[1]).filterBounds(geometry)
    features = dataset.getInfo()
    length = len(features['features'])
    ids, dates = [], []
    for i in range(0, (length)):
        name = features['features'][i]['id']
        date = name[-2:] + '/' + name[-4:-2] + '/' + name[-8:-4]
        ids.append(name)                                        
        dates.append(date)
        dates = ['Selecione'] + remove_duplicates_list(dates)
        date_r =  date[-4:] + date[-7:-5] + date[-10:-8]
        select_ids = []
        for id in ids:
            if date_r in id:
                select_ids.append(id)
    return length, dates, select_ids