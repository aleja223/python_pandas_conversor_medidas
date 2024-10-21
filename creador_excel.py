import pandas as pd


# Dataframe es la informacion basica con las piezas y centrimetros para poder armar el excel

data = {
    "Piezas:" :["Pata", "Tablero", "Puerta","Estante", "Panel lateral"],
    "Centrimetros" :[40,120,60,30,180]
}

df = pd.DataFrame(data)

#Guardar el Dataframe en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)