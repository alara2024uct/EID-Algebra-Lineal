#Flujo de trabajo del código

import os
import pandas as pd
from carga_datos import cargar, cargar_peliculas
from generador_matrices import convertir_a_matriz, calculo_matriz_similitud
from recomendaciones import recomendaciones
from graficos import grafica_distribucion_calificaciones, grafica_mapa_calor_similitud, grafica_frecuencia_recomendaciones


def ejecutar_sistema():

    ruta_ratings = "archivos/ratings.csv"   #Ruta archivo de ratings
    ruta_movies = "archivos/movies.csv"     #Ruta archivo de movies
    
    datos_ratings = cargar(ruta_ratings)           #Carga los datos
    datos_movies = cargar_peliculas(ruta_movies)
    
    if datos_ratings.empty or datos_movies.empty:    #Verifica que no sean archivos vacios
        print("No se pudieron cargar los archivos")  #Si no arroja un error
        return

    matriz_usuario_producto = convertir_a_matriz(datos_ratings)   #Construye matriz usuario-producto

    matriz_similitud = calculo_matriz_similitud(matriz_usuario_producto)  #Calculo de matriz similitud
    
    id_usuario_objetivo = 4                 #Especificamos al usuario objetivo
    print(f"Generando demostración para el informe con el Usuario {id_usuario_objetivo}")
    top_sugerencias = recomendaciones(
        usuario_especifico=id_usuario_objetivo, 
        matriz_usuario_producto=matriz_usuario_producto, 
        matriz_similitud=matriz_similitud, 
        n_recomendaciones=3
    )
    
    print(f"Recomendacion para el usuario: {id_usuario_objetivo}")
    if not top_sugerencias.empty:
        for rango, (id_pelicula, puntaje) in enumerate(top_sugerencias.items(), 1):   
            titulo_row = datos_movies[datos_movies['movieId'] == id_pelicula]       #Realiza busqueda por ID de pelicula
            titulo = titulo_row['title'].values[0] if not titulo_row.empty else f"ID: {id_pelicula}"  #Extrae el titulo de la pelicula
            print(f"Top {rango} -> {titulo} (Puntaje Predicho: {puntaje:.2f})")       #Muestra 
    else:
        print("No hay recomendaciones para mostrar.")

    print("Tercer grafico con multiples usuarios:")
    items_sugeridos = []  #Lista para sugerencias
    
    usuarios_muestra = matriz_usuario_producto.index[:15]   #Toma los primeros 15 usuarios para tendencias
    
    for user in usuarios_muestra:
        # Ejecutamos el algoritmo para el usuario actual
        top_sug = recomendaciones(usuario_especifico=user, matriz_usuario_producto=matriz_usuario_producto
                                  , matriz_similitud=matriz_similitud, n_recomendaciones=3)
        if not top_sug.empty:
            for id_pelicula in top_sug.index:
                titulo_row = datos_movies[datos_movies['movieId'] == id_pelicula]  #Busca nombre de pelicula por su ID
                if not titulo_row.empty:
                    titulo_real = titulo_row['title'].values[0]
                    items_sugeridos.append(titulo_real)
                else:
                    items_sugeridos.append(f"ID: {id_pelicula}")

   
    grafica_distribucion_calificaciones(datos_ratings) #Genera el grafico de distribucion con el .csv del rating
    
    grafica_mapa_calor_similitud(matriz_similitud) #Genera el mapa de calor usando la matriz similitud
    
    grafica_frecuencia_recomendaciones(items_sugeridos) #Genera el grafico de las recomendaciones

    print("Graficos ejecutados exitosamente")

if __name__ == "__main__":
    ejecutar_sistema()