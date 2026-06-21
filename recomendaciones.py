from generador_matrices import calculo_matriz_similitud
import pandas as pd
import numpy as np

def recomendaciones(usuario_especifico, matriz_usuario_producto, matriz_similitud, n_recomendaciones=3):  #Funcion para las recomendaciones
    print(f"Generando recomendaciones para el usuario {usuario_especifico}...")

    vistos = matriz_usuario_producto.loc[usuario_especifico]   #Identifica si el usuario vio/utilizo el producto
    no_vistos = vistos[vistos == 0].index                      #Verifica los 0s en la matriz para identificar que no vio/utilizo el producto
    
    if len(no_vistos) == 0:
        print(f"El usuario {usuario_especifico} ya ha consumido todos los productos disponibles.")
        return pd.Series(dtype=float)

    vecinos_similares = matriz_similitud[usuario_especifico].drop(usuario_especifico) 
    
    matriz_vecinos_productos = matriz_usuario_producto.loc[vecinos_similares.index, no_vistos]
    
    numerador = np.dot(vecinos_similares, matriz_vecinos_productos)
    
    denominador = np.dot(vecinos_similares, matriz_vecinos_productos > 0)
    
    denominador = np.where(denominador == 0, 1e-9, denominador)
    
    puntajes = numerador / denominador
    
    recomendaciones_ordenadas = pd.Series(puntajes, index=no_vistos).sort_values(ascending=False)
    
    return recomendaciones_ordenadas.head(n_recomendaciones)