import streamlit as st
from airtable import Airtable
import pandas as pd
import folium
from streamlit_folium import folium_static

# Connexion a la airtable
base_id = 'appLzsnUVJ5A1rdRo'
table_name = 'images'
api_key = 'patxhc37ccrHiEXmN.c8cea3b4af146d70fcdf3efaf4508cbba2c2ecb90765887c15dad50f47f5a436'
airtable = Airtable(base_id, table_name, api_key)

#test pour recuperer les images de la table
records = airtable.get_all()
for record in tqdm(records):
    st.write(record['fields'])

# Convertir les données en DataFrame Pandas
data = pd.DataFrame([record['fields'] for record in records])

def mapp():
    st.title('Carte des déchets sauvages')
    #initialize the map contered around Mantes-la-Jolie
    m = folium.Map(location=[48.9900,1.7200], zoom_start=14)
    for idx, row in data.iterrow():
        folium.Marker([row['lat'], row['lon']], popup = row['photo']).add_to(m)

    folium_static(m)
