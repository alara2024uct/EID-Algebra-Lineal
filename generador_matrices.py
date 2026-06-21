#Modulo para generar las diferentes matrices

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def convertir_a_matriz(df: pd.DataFrame) -> pd.DataFrame:        #Convierte los datos cargados a una matriz

    if df.empty:
        print("Datos vacios, no se pudo construir la matriz")    #Verifica que hayan datos en el archivo cargado
        return pd.DataFrame
    
    print("Construyendo matriz")

    matriz = df.pivot(
                      index='id_usuario', 
                      columns='id_pelicula',       #Construye la matriz
                      values='calificacion'
                      )

    matriz = matriz.fillna(0)      #Rellena espacio vacios con 0s
    print("Matriz creada correctamente")
    return matriz      #Devuelve la matriz


def calculo_matriz_similitud(matriz_usuario_producto: pd.DataFrame) -> pd.DataFrame:   #Calcula la matriz similitud para

    print("Calculando matriz similitud")

    valores_matriz = cosine_similarity(matriz_usuario_producto)   #Calcula valores de la matriz utilizando la funcion cosine_similarity

    usuarios = matriz_usuario_producto.index             #Extrae los IDs de los usuarios y los guarda en la variable
    matriz_similitud = pd.DataFrame(valores_matriz, index = usuarios, columns = usuarios)   #Convierte la matriz en un DataFrame

    print(f"matriz: {matriz_similitud.shape}")
    return matriz_similitud                     #Devuelve la matriz

