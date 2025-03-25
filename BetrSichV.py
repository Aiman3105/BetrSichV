import streamlit as st
import Funktionen_BetrSichV

st.title("Einstufung nach BetrSichV:")


FG=st.text_input(label="", placeholder="Fluidgruppe",  key="Fluidgruppe")
AZ=st.text_input(label="", placeholder="Aggregatzustand",  key="Aggregatzustand")
PS=st.text_input(label="", placeholder="zul Druck",  key="zul Druck")
DN=st.text_input(label="", placeholder="DN",  key="DN")



if FG is not "" and AZ is not "" and PS is not "" and DN is not "":
    Prüfungen_nach_Nr4, Prüfungen_nach_Nr5 = Funktionen_BetrSichV.BetrSichV_RL(int(FG), AZ, int(PS), int(DN))
    st.text_input("Prüfungen nach Nr 4:", Prüfungen_nach_Nr4, disabled=True)
    st.text_input("Prüfungen nach Nr 5:", Prüfungen_nach_Nr5, disabled=True)