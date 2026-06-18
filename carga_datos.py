#Módulo para carga de datos 

import pandas as pd    

def cargar(ruta: str) -> pd.DataFrame:

    print("Intentando cargar datos")

    try:
        df = pd.read_csv(ruta)                   #Lee el archivo y lo convierte a formato tabla
        print("Datos cargados correctamente")
        return df

    except FileNotFoundError:
        print("No se pudo cargar el archivo")
        return pd.DataFrame


def convertir_a_matriz(df: pd.DataFrame) -> pd.DataFrame:

    if df.empty:
        print("Datos vacios, no se pudo construir la matriz")
        return pd.DataFrame
    

    print("Construyendo matriz")

    matriz = df.pivot(
                      index='id_usuario', 
                      columns='id_pelicula',
                      values='calificacion'
                      )

    matriz = matriz.fillna(0)      #Rellena espacio vacios con 0s

    print("Matriz creada correctamente")

    return matriz      #Devuelve la matriz



    
