#Módulo para carga de datos 

import pandas as pd        #Importa modulo pandas para trabajar con el archivo con los datos a cargar

def cargar(ruta: str) -> pd.DataFrame:

    print("Intentando cargar datos")

    try:
        df = pd.read_csv(ruta)                   #Lee el archivo y lo convierte a formato tabla
        print("Datos cargados correctamente")
        return df

    except FileNotFoundError:
        print("No se pudo cargar el archivo")    #Si no encuentra el archivo, arroja un error
        return pd.DataFrame
    
def cargar_peliculas(ruta: str) -> pd.DataFrame:   #Funcion para cargar el .csv de las peliculas

    print(f"Cargando peliculas")
    return pd.read_csv(ruta)      #Lee la ruta del archivo



    
