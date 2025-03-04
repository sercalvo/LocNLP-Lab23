# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:05:33 2023

@author: Sergio
"""

import streamlit as st
import spacy
import re
import io

st.set_page_config(
    page_title="LocNLP23Lab - Feature Extraction",
    page_icon="img//V-Logo-icon48.png",
)

# Load the 'en_core_web_sm' model
nlp = spacy.load('en_core_web_sm')

# Create a Streamlit app
st.title(":red_circle: Feature Extraction :magnet:")
st.markdown("""This app makes use of `Spacy`, `re` and `Streamlit` libraries to extract relevant information from a text. Feature extraction involves reducing the number of elements required to understand large datasets for text analysis, statistics and information extraction.""")

# Header
st.header("Add a text for analysis")
# Allow the user to paste a text, use the example text, or upload a file
option = st.radio('Choose input type:', ['Paste text', 'Select sample data', 'Upload file'], help="Only clean text format (.txt file)")
if option == "Paste text":
    text = st.text_area("Paste your text here", "")
elif option == "Select sample data":
    sample_data = {
        "Sample text 1 - Cards": "John Smith works for Google in Mountain View, California. He can be reached at john.smith@gmail.com.",
        "Sample text 2 - Sports": "Bonucci, whose contract expires next season, began his career at Inter Milan in 2005, where he won his first Serie A title in 2005-06. The defender also had spells at Treviso, Pisa, Genoa and Bari before joining Juventus in 2010, becoming part of a famous Juve backline along with Andrea Barzagli, Giorgio Chiellini and goalkeeper Gianluigi Buffon that dominated Italian football for a decade. The Turin giants won nine successive titles between 2011-12 and 2019-20, with Bonucci claiming eight of those after spending one season at AC Milan in 2017-18. Bonucci made his Italy debut in March 2010 and captained the side for the first time four years later. He represented the Azzurri at two World Cups and three European Championships, finishing runner-up at Euro 2012 before lifting the trophy nine years later following a penalty shootout win over England at Wembley.",
        "Sample text 3 - Emails": """From: Jessica Adams jessica.adams@globaltech.com
                                            To: Michael Thompson michael.thompson@innovateai.io
                                            CC: Emily Carter emily.carter@marketingedge.com
                                            Subject: Partnership Discussion – AI Solutions

                                            Dear Michael,

                                            I hope you're doing well. I'm reaching out regarding a potential collaboration between GlobalTech Solutions and InnovateAI Inc. on advanced natural language processing (NLP) solutions.

                                            We recently launched a new AI-driven analytics platform, and we believe your expertise in machine learning could bring significant value to this initiative. Would you be available for a virtual meeting next Wednesday, March 20, at 2:00 PM EST?

                                            If you prefer an in-person discussion, I will be in San Francisco from March 18-22, staying at the Hilton San Francisco Union Square, located at 333 O'Farrell Street, San Francisco, CA 94102.

                                            Let me know what works best for you. Feel free to reach me at jessica.adams@globaltech.com or my assistant, Emily Carter (emily.carter@marketingedge.com), for scheduling details.

                                            Looking forward to your response.

                                            Best regards,
                                            Jessica Adams
                                            Senior AI Strategist
                                            GlobalTech Solutions
                                            Office: 415-555-0198
                                            Website: www.globaltech.com""",
        }
    selected_sample = st.selectbox('Select sample data', list(sample_data.keys()))
    text = sample_data[selected_sample]
elif option == "Upload file":
    file = st.file_uploader("Choose a file")
    # Get the contents of the file as a string
    if file:
        
        # To convert to a string based IO:
        stringio = io.StringIO(file.getvalue().decode("utf-8"))    
        # To read file as string:
        string_data = stringio.read()
        text = " ".join(string_data.split()) 
        #text = st.io.get_value(file)
    else:
        text = ''
        

if text:
    # Display the selected text
    st.subheader("Text to analyze")
    st.caption("Showing only first 1000 words in the text")
    words = text.split()[:1000]
    limited_text = ' '.join(words)
    st.markdown(f'<div style="height: 150px; overflow-y: scroll;">{limited_text}</div>', unsafe_allow_html=True)

st.divider()

# Process the text
if st.button("Extract information from text"):
    doc = nlp(text)

    # Extract features
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    unique_names = set()
    unique_organizations = set()
    unique_locations = set()
    unique_emails = set()
    
    for entity, label in entities:
        if label == "PERSON":
            unique_names.add(entity)
        elif label == "ORG":
            unique_organizations.add(entity)
        elif label == "GPE":
            unique_locations.add(entity)
    
    names_list = list(unique_names)
    organization_list = list(unique_organizations)
    location_list = list(unique_locations)


    

    # Find emails using regular expression
    email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text) or []
    for email in email_list:
        if email in unique_names:
            continue
        unique_emails.add(email)  

    email_list = list(unique_emails)

    # Display the results
    st.header("Information extraction results")
    if names_list:
        st.markdown("**:orange[Person Names:]**")
        for name in names_list:
            st.write("- " + name)
    else:
        st.caption(":red[**No person names** found in the text]")

    if organization_list:
        st.write("**:green[Organizations:]**")
        for organization in organization_list:
            st.write(" - " + organization)
    else:
        st.caption(":red[**No organizations** found in the text]")

    if location_list:
        st.write("**:blue[Locations:]**")
        for location in location_list:
            st.write("- " + location)
    else:
        st.caption(":red[**No locations** found in the text]")

    if email_list:
        st.write("**:violet[Emails:]**")
        for email in email_list:
            st.write("- " + email)
    else:
        st.caption(":red[**No emails** found in the text]")
