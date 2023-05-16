import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image
import os, shutil


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# Page Heading
st.image("images/head.png", width = 700)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Summary", "TeleHealth Appointments", "Chart Review", "Results", "Notes", "Education", "Care Plan",
                                              "Orders", "Navigation"])

# Sidebar Details
with st.sidebar:
    selected = option_menu("Main Menu", ['Patient Information', 'Appointments', 'Notes and Alerts'],
        icons=['house', 'cloud-upload', "list-task", 'gear', 'bell'],
                           menu_icon="cast", default_index=1)

    local_css("style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    icon("search")
    selected = st.text_input("Enter patient full name", "Search...")
    button_clicked = st.button("OK")

with tab1:
    if button_clicked:
        st.markdown(
            """
            <style>
                [data-testid=stSidebar] [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 50%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        #st.image("images/hp_headshot.jpeg", width = 150)
        # st.markdown('Patient Name: **Harry Potter**')
        # st.markdown('Age: **30**')
        # st.markdown('DOB: **January 17th, 1993**')
        # st.write('   ')

        # Fill in text boxes
        # Top text boxes
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            first_name = st.text_input("First Name", "Harry", key=1)
            dob = st.text_input("DOB", "01/07/1993", key=2)
        with col2:
            last_name = st.text_input("Last Name", "Potter", key=3)
            age = st.text_input("Age", "30", key=4)
        with col3:
            patient_id = st.text_input("Patient ID", "442832", key=5)
            allergies = st.text_input("Allergies", "None", key=6)

        summary = st.text_area("Add visit summary", height=100)

    else:
        # Top text boxes
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            first_name_2 = st.text_input("First Name", key=7)
            dob_2 = st.text_input("DOB", key=8)
        with col2:
            last_name_2 = st.text_input("Last Name", key=9)
            age_2 = st.text_input("Age", key=10)
        with col3:
            patient_id_2 = st.text_input("Patient ID", key=11)
            allergies_2 = st.text_input("Allergies", key=12)

        summary = st.text_area("Summary", height=100)






