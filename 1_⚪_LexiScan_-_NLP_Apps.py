# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:59:10 2022

@author: Sergio
"""

import time
import os
from os import path
import streamlit as st
import streamlit.components.v1 as components
# La configuración de la página debe estar en la PRIMERA línea después de las importaciones
st.set_page_config(
    page_title="LocNLP Lab", 
    layout="wide",
    page_icon="img//V-Logo-icon48.png",)

# Google Analytics
GA_ID = "G-K1YQS7TZCV"  # Reemplázalo con tu ID de Google Analytics
GA_SCRIPT = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{GA_ID}', {{ 'anonymize_ip': true }});
    </script>
"""

components.html(GA_SCRIPT, height=0, scrolling=False)


from PIL import Image

# A helloworld
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
page_logo = Image.open(path.join(d, 'img//LocNLPlab23.png'))


with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.image(page_logo) 
st.markdown(
    """
    # NLP and Localization LAB
    \n### Welcome to the place where I test my NLP ideas!
    \nYou will find some kind of magic, but it's a matter of believing or not. I do believe in the magic of computational linguistics and natural language processing.
    \nI'm sharing a few examples of how using Python and some available libraries and resources, a few things can be done. 
    I have built this app using `Streamlit`, an open-source app framework built specifically for
    Machine Learning and Data Science projects. Behind, there's a full range of libraries and Python code, of course. I am not an expert, but do take advantage of libraries like `Spacy`, `NLTK`, `Transformers`, `Pandas`, `scikit-learn`, `Beautiful Soup`, `TextBlob`, `Gensim`, `PyTorch` and many others!
    \nThe goal? Unveil the secrets of languages, no matter if they are meant for humans or computers. The main NLP applications that you will find in this web app are:
         \n`Tokenization`, `Lemmatization`, `Embeddings and vectorization`, `Part of Speech and dependency analyzer`, `Feature extraction`, `Text generation`, `Sentiment analysis`, `Term extraction`
         \nNew ideas are often like waves returning all the time to embrace the shore. I will be in the beach waiting for the new wave. There is plenty of ideas to surf!
    
    \nEnjoy the ride! 	:bike:
    \n:smiley: Sergio Calvo
"""
)

with st.expander("About Sergio"):
    st.write("""Translator, reviewer and computational linguist with 20+ years of experience in multiple translation and localization areas, NLP (Natural Language Processing) and localization engineering. He is passionate for going deep in the entrails of any language, either spoken by humans or computers, to unveil the beauty of communication.
             \n Get more info at [www.veriloquium.com](https://www.veriloquium.com)""")

st.markdown(
    """
   \n
   \n### Want to learn more?
   \n**👈 Select a demo from the sidebar** to see some NLP app examples!
   """
   )