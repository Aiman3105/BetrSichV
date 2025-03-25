import streamlit as st
import Funktionen_BetrSichV



FG=0
st.title("Einstufung nach BetrSichV:")

st.text("H-Sätze:")
H_1=st.checkbox("H224, H225, H226 (T_zul > T_FP & T_FP <= 55°C), "
                "H250, H300, H310, H330", key="H_1")
H_2=st.checkbox("H226 (T_zul < T_FP & T_FP <= 55°C), H314", key="H_2")

if H_1:
    FG=1
if H_2:
    FG=1.5



#FG=st.text_input(label="", placeholder="Fluidgruppe",  key="Fluidgruppe")
AZ=st.text_input(label="", placeholder="Aggregatzustand",  key="Aggregatzustand")
PS=st.text_input(label="", placeholder="zul Druck",  key="zul Druck")
DN=st.text_input(label="", placeholder="DN",  key="DN")



if FG is not "" and AZ is not "" and PS is not "" and DN is not "":
    Prüfungen_nach_Nr4, Prüfungen_nach_Nr5 = Funktionen_BetrSichV.BetrSichV_RL(int(FG), AZ, int(PS), int(DN))
    st.text_input("Prüfungen nach Nr 4:", Prüfungen_nach_Nr4, disabled=True)
    st.text_input("Prüfungen nach Nr 5:", Prüfungen_nach_Nr5, disabled=True)