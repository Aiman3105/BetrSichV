import streamlit as st
import Funktionen_BetrSichV



FG=0
AZ=""
H_0=0
H_1=0
H_2=0
H_3=0
FG_1=0
FG_2=0
st.title("Einstufung nach BetrSichV:")

st.markdown("**Druckgerät:**")
col_App, col_RL= st.columns(2)

with col_App:
    Apparate = st.checkbox("Apparate", key="Apparate")
with col_RL:
    Rohrleitungen = st.checkbox("Rohrleitungen", key="Rohrleitungen")

if Apparate and Rohrleitungen:
    st.error("Bitte nur eine Checkbox unter Druckgerät auswählen")



col1, col2= st.columns(2)

#Aggregatzustände
with col1:
    st.markdown("**Aggregatzustand**")
    gasförmig = st.checkbox("gasförmig", key="gasförmig")
    flüssig = st.checkbox("flüssig", key="flüssig")

if gasförmig:
    AZ = "g"
if flüssig:
    AZ = "f"
if gasförmig and flüssig:
    st.error("Bitte nur eine Checkbox unter Aggregatzustand auswählen")


#H-Sätze
with col2:

    if Rohrleitungen:
        st.markdown("**H-Sätze:**")
        if AZ=="g":
            H_0 = st.checkbox("akut toxisch: H300, H310, H330", key="H_0")
            H_1 = st.checkbox("H224, H225, H226 (T_zul > T_FP & T_FP <= 55°C)", key="H_1")
        else:
            H_1 = st.checkbox("H224, H225, H226 (T_zul > T_FP & T_FP <= 55°C), "
                              "H250, H300, H310, H330", key="H_1")
        H_2 = st.checkbox("H226 (T_zul < T_FP & T_FP <= 55°C), H314", key="H_2")
        H_3 = st.checkbox("Alle anderen Medien", key="H_3")

        if H_0:
            FG = 0.5
        if H_1:
            FG = 1
        if H_2:
            FG = 1.5
        if H_3:
            FG = 2

    if Apparate:
        st.markdown("**Fluidgruppe**")
        FG_1 = st.checkbox("1", key="FG_1")
        FG_2 = st.checkbox("2", key="FG_2")

        if FG_1:
            FG=1
        if FG_2:
            FG=2



    #Bestimmung Fluidgruppe für Formel


checked_count_H = sum([H_0, H_1, H_2, H_3])
if checked_count_H>1:
    st.error("Bitte nur eine Checkbox unter H-Sätze auswählen")

checked_count_FG = sum([FG_1, FG_2])
if checked_count_FG>1:
    st.error("Bitte nur eine Checkbox unter Fluidgruppe auswählen")


#Zulässiger Druck und Nennweite/Volumen
if Rohrleitungen:
    DN=st.text_input(label="", placeholder="Nennweite [DN]",  key="DN")
if Apparate:
    V=st.text_input(label="", placeholder="Volumen [L]",  key="V")
PS=st.text_input(label="", placeholder="Zulässiger Betriebsdruck [barg]",  key="zul Druck")



#Einstufung Rohrleitungen
col_Eintufung_Nr4, col_Eintufung_Nr5=st.columns(2)
if Rohrleitungen:
    if FG is not "" and AZ is not "" and PS is not "" and DN is not "":
        Prüfungen_nach_Nr4, Prüfungen_nach_Nr5 = Funktionen_BetrSichV.BetrSichV_RL(float(FG), AZ, float(PS), float(DN))
        with col_Eintufung_Nr4:
            st.text_input("Prüfungen nach Nr 4:", Prüfungen_nach_Nr4, disabled=True)
        with col_Eintufung_Nr5:
            st.text_input("Prüfungen nach Nr 5:", Prüfungen_nach_Nr5, disabled=True)

#Einstufung Apparate
if Apparate:
    if FG is not "" and AZ is not "" and PS is not "" and V is not "":
        Prüfungen_nach_Nr4, Prüfungen_nach_Nr5 = Funktionen_BetrSichV.BetrSichV_AP(float(FG), AZ, float(PS), float(V))
        with col_Eintufung_Nr4:
            st.text_input("Prüfungen nach Nr 4:", Prüfungen_nach_Nr4, disabled=True)
        with col_Eintufung_Nr5:
            st.text_input("Prüfungen nach Nr 5:", Prüfungen_nach_Nr5, disabled=True)

