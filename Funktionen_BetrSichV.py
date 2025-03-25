

#Rohrleitungen



def BetrSichV_RL(FG, AZ, PS, DN):
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

    #akut toxisch Tabelle 8 H300, H310, H330
    if FG==0.5 and AZ=="g":
        if DN>25 and PS>0.5:
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

def BetrSichV_AP(FG, AZ, PS, V):
    #Tabelle3
    if FG == 1 and AZ == "g":
        if V>1 and V<=200 and PS>0.5 and PS*V>25 and PS*V<=200:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V>200 and PS>0.5 and PS<= 1:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V<=1 and PS>200 and PS<=1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif V>1 and PS>1 and PS*V>200 and PS*V<=1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif V<=1 and PS>1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        elif V>1 and PS>1 and PS*V>1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #Tabelle 4
    if FG==2 and AZ=="g":
        if V>1 and V<=200 and PS>0.5 and PS*V>50 and PS*V<=200:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V>200 and PS>0.5 and PS<= 1:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V>1 and PS>1 and PS*V>200 and PS*V<=1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif V<=1 and PS>1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        elif V>1 and PS>1 and PS*V>1000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #tabelle 5
    if FG == 1 and AZ == "f":
        if PS>0.5 and PS<=10 and PS*V>200:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V<=1 and PS>500 and PS*V<=1000:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V<=1 and PS>500 and PS*V>1000 and PS*V<=10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif V>1 and PS>500 and PS*V<=10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif V>1 and PS>10 and PS<=500 and PS*V>200:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif PS>500 and PS*V>10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    #tabelle 6
    if FG == 2 and AZ == "f":
        if V<=1 and PS>1000 and PS*V<=1000:
            Pr_Nr4 = "bP"
            Pr_Nr5 = "bP"
        elif V<=10 and PS>1000 and PS*V>1000 and PS*V<=10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif PS>10 and PS<=500 and PS*V>10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "bP"
        elif PS>500 and PS*V>10000:
            Pr_Nr4 = "ZÜS"
            Pr_Nr5 = "ZÜS"
        else:
            Pr_Nr4 = "AM"
            Pr_Nr5 = "AM"

    return Pr_Nr4, Pr_Nr5


