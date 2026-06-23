#Módulo para graficas

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use('seaborn-v0_8-whitegrid')  #Configuracion de estilo grafico

def grafica_mapa_calor_similitud(matriz_similitud: pd.DataFrame):

    plt.figure(figsize=(9, 7))
    
    muestra_usuarios = matriz_similitud.iloc[:12, :12]   #Toma solo los primeros 12
    
    sns.heatmap(muestra_usuarios, annot=True, cmap='Blues', fmt=".2f", cbar=True,
                annot_kws={"size": 9, "weight": "bold"})   #Estilos graficos
    
    plt.title('Mapa de Calor: Similitud Coseno (Muestra de Usuarios)', fontsize=12, fontweight='bold', pad=15)  #Titulo del grafico
    plt.xlabel('ID Usuario', fontsize=10)   #Label eje x
    plt.ylabel('ID Usuario', fontsize=10)   #Label eje y
    plt.tight_layout()
    plt.savefig('archivos/heatmap_similitud.png', dpi=300)   #Guarda una imagen del grafico en .png a alta resolución
    plt.show()     #Muestra graficamente

def grafica_distribucion_calificaciones(df_datos: pd.DataFrame):   #Realiza un EDA (Analisis exploratorio de Datos)

    plt.figure(figsize=(7, 4))
    
    sns.countplot(x='rating', data=df_datos, hue='rating', palette='Blues_d', legend=False)     #Cuenta la frecuencia de cada calificacion
    
    plt.title('Distribución de las Calificaciones en el Dataset', fontsize=12, fontweight='bold', pad=10)   #Titulo grafico
    plt.xlabel('Calificación', fontsize=10)        #Label eje x
    plt.ylabel('Cantidad de Votos', fontsize=10)   #Label eje y
    
    # Suavizamos las líneas de la grilla para que no compitan con las barras
    plt.grid(axis='y', linestyle=':', alpha=0.6, color='#CCCCCC')
    sns.despine(left=True, bottom=True) # Remueve los bordes negros innecesarios
    
    plt.tight_layout()
    plt.savefig('archivos/distribucion_calificaciones.png', dpi=300)       #Guarda una imagen del grafico en .png
    plt.show()     #Muestra gráficamente

def grafica_frecuencia_recomendaciones(recomendaciones: list):    #Grafico de películas más recomendadas

    if not recomendaciones:
        print("No hay datos para la frecuencia")
        return
        
    plt.figure(figsize=(10, 5))   #Tamaño de figura
    
    # Contamos la frecuencia de aparición de cada elemento
    series_items = pd.Series(recomendaciones)
    top_items = series_items.value_counts().head(10)
    
    # Grafica usando la paleta 'GnBu_d' (un elegante degradado turquesa a azul oscuro)
    sns.barplot(x=top_items.values, y=top_items.index.astype(str), hue=top_items.index.astype(str), palette='GnBu_d', legend=False)
    
    plt.title('Top 10 Películas Recomendadas', fontsize=12, fontweight='bold', pad=12) #Titulo grafico
    plt.xlabel('Número de veces recomendada', fontsize=10)  #Label eje x
    plt.ylabel('Película', fontsize=10)                     #Label eje y
    plt.grid(axis='x', linestyle=':', alpha=0.6, color='#CCCCCC')   
    sns.despine(left=True, bottom=True)
    
    plt.tight_layout()       #Evita que los nombres largos se corten
    plt.savefig('archivos/frecuencia_recomendaciones.png', dpi=300)   #Guarda una foto del gráfico como un .png
    plt.show()    #Muestra visualmente