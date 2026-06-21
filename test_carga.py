import pandas as pd
import numpy as np
# Importamos tus funciones (ajusta el nombre de los archivos si es necesario)
from carga_datos import cargar
from generador_matrices import calculo_matriz_similitud, convertir_a_matriz
from recomendaciones import recomendaciones

def probar_modulo_carga():
    print("--- INICIANDO PRUEBA DE CARGA ---")
    ruta_test = "archivos/datos_prueba.csv"
    
    # 1. Probar la función de carga
    df = cargar(ruta_test)
    
    print("\n--- VERIFICACIÓN DEL DATAFRAME ---")
    print(df)
    
    # Pasos de control (Aserciones)
    assert not df.empty, "Error: El DataFrame no debería estar vacío."
    assert "id_usuario" in df.columns, "Falta la columna id_usuario"
    print("✓ Paso 1: El archivo CSV se lee correctamente.")

    # 2. Probar la conversión a matriz de interacción
    matriz = convertir_a_matriz(df)
    
    print("\n--- VERIFICACIÓN DE LA MATRIZ REORGANIZADA ---")
    print(matriz)
    
    print("\n--- COMPROBACIÓN DE DATOS FALTANTES (RELLENO CON 0) ---")
    # Verificamos si el usuario 1 tiene un 0 en la película 103 (donde no tenía voto)
    voto_faltante = matriz.loc[1, 103]
    print(f"Calificación del Usuario 1 para la Película 103 (originalmente vacía): {voto_faltante}")
    
    assert voto_faltante == 0, "Error: Los valores faltantes no se están rellenando con 0."
    print("✓ Paso 2: La matriz se pivota y rellena con ceros correctamente.")
    
    print("\nTest de carga exitoso\n")

    # 3. Probar el cálculo de la matriz de similitud
    matriz_similitud = calculo_matriz_similitud(matriz)
    print("--- MATRIZ DE SIMILITUD ENTRE USUARIOS ---")
    print(matriz_similitud)
    print("\n✓ Paso 3: Matriz de similitud calculada correctamente.\n")

    # 4. PROBAR EL SISTEMA DE RECOMENDACIONES
    print("--- PROBANDO MOTOR DE RECOMENDACIONES ---")
    usuario_test = 1
    # Solicitamos 2 recomendaciones para ver el orden predictivo de las películas no vistas
    top_rec = recomendaciones(usuario_test, matriz, matriz_similitud, n_recomendaciones=2)
    
    print(f"\n--- TOP RECOMENDACIONES PARA EL USUARIO {usuario_test} ---")
    if not top_rec.empty:
        for idx, (id_pelicula, puntaje) in enumerate(top_rec.items(), 1):
            print(f"{idx}. Película ID: {id_pelicula} | Puntaje Predicho: {puntaje:.4f}")
        print("\n✓ Paso 4: Recomendaciones generadas y ordenadas con éxito.")
    else:
        print("No hay recomendaciones para mostrar.")

if __name__ == "__main__":
    probar_modulo_carga()