

#Rohrleitungen



def BetrSichV_RL(FG, AZ, PS, DN):
    #ggfs. Fluidgruppe durch H-Sätze ersetzen
    #akut toxisch muss noch ergänzt werden

    #Fluidgruppe 2 raus
    if FG==2:
        Pr_Nr4 = "AM"
        Pr_Nr5 = "AM"

    #Tabelle 8
    #H220, H221, H224, H225, H226(max. zul Temp.>Flammpunkt + Flammpunkt<55°C),
    #H250, H300, H310, H330

    if FG==1 and AZ=="g":
        if DN>25 and PS>0.5 and DN*PS<=2000:
            Pr_Nr4="bP"
            Pr_Nr5="bP"
        elif DN>25 and PS>0.5 and DN*PS>2000:
            Pr_Nr4="ZÜS"
            Pr_Nr5="ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #Tabelle 9
    #H226 (max. zul Temp.<Flammpunkt + Flammpunkt<55°C), H314
    if FG==1.5 and AZ=="g":
        if DN>32 and PS>0.5 and DN*PS>1000 and DN*PS<=2000:
            Pr_Nr4="bP"
            Pr_Nr5="bP"
        elif DN>32 and PS>0.5 and DN*PS>2000:
            Pr_Nr4="ZÜS"
            Pr_Nr5="ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #Tabelle 10
    #H224, H225, H226(max. zul Temp.>Flammpunkt + Flammpunkt<55°C),
    #H250, H300, H310, H330
    if FG==1 and AZ=="f":
        if DN>25 and PS>0.5 and DN*PS>2000:
            Pr_Nr4="ZÜS"
            Pr_Nr5="ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #Tabelle 11
    #H226 (max. zul Temp.<Flammpunkt + Flammpunkt<55°C), H314
    if FG==1.5 and AZ=="f":
        if DN>200 and PS>10 and DN*PS>5000:
            Pr_Nr4="ZÜS"
            Pr_Nr5="ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"


    return Pr_Nr4, Pr_Nr5

