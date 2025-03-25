import streamlit as st
import Funktionen_BetrSichV

st.title("Einstufung nach BetrSichV")


st.text_input(label="", placeholder="Fluidgruppe",  key="Fluidgruppe")
st.text_input(label="", placeholder="Aggregatzustand",  key="Aggregatzustand")
st.text_input(label="", placeholder="zul Druck",  key="zul Druck")
st.text_input(label="", placeholder="DN",  key="DN")
