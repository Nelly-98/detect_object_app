import streamlit as st
from PIL import Image
import cv2
import tempfile
import numpy as np
from airtable import Airtable
from tqdm import tqdm
import requests
import cloudinary
import cloudinary.uploader

#connexion avec la base de donnees airtable
'''base_id = 'appLzsnUVJ5A1rdRo'
table_name = 'images'
api_key = 'patxhc37ccrHiEXmN.c8cea3b4af146d70fcdf3efaf4508cbba2c2ecb90765887c15dad50f47f5a436'
airtable = Airtable(base_id, table_name, api_key)'''

#test pour recuperer les images de la table
#records = airtable.get_all()
#for record in tqdm(records):
    #st.write(record['fields'])
        

'''def upload_to_img_hosting_service(uploaded_image):
    cloudinary.config(
        cloud_name = "drmonzs9y", 
        api_key = "513988441526899", 
        api_secret = "kt7qF_5sTiR0C0T4PK6OHdasPjk"
        )

    upload_result = cloudinary.uploader.upload(uploaded_image)
    return upload_result['url']
'''

def object_detect():
    st.title('Détection de déchets')

    #st.markdown("""<style>div.row-widget.stRadio > div{flex-direction:row;}</style>""", unsafe_allow_html=True)

    choix = st.radio("Choisissez le mode d'entrée :", ('Uploader une Image', 'Uploader une Vidéo', 'Caméra Vidéo'))

    if choix == 'Uploader une Image':
        uploaded_image = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
           col1, col2 = st.columns(2)
           with col1 : 
                image = Image.open(uploaded_image)
                st.image(image, caption='Image uploadée', use_column_width=True)
                #detect_button = st.button('Cliquez Ici pour Détecter l\'objet')
            # Traitement de détection d'objets
            #if st.button('Détecter l\'objet'):
                # Code pour la détection d'objet sur l'image
            #detect_button = st.button('Cliquez Ici pour Détecter l\'objet')
            # Traitement de détection d'objets
            #if st.button('Détecter l\'objet'):
                # Code pour la détection d'objet sur l'image

    elif choix == 'Uploader une Vidéo':
        uploaded_video = st.file_uploader("Choisissez une vidéo...", type=["mp4", "avi", "mov"])
        if uploaded_video is not None:
            col1, col2 = st.columns(2)
            with col1 :
                #video = Image.open(uploaded_video)
                st.video(uploaded_video, caption='Vidéo Uploadée', use_column_width=True)
            #if st.button('Détecter l\'objet'):
                # Code pour la détection d'objet sur la vidéo

    #elif choix == 'Caméra Vidéo':
        # Code pour la capture vidéo de la caméra
        #if st.button('Détecter l\'objet'):
            # Code pour la détection d'objet à partir de la caméra


    