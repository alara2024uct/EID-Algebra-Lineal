import pandas as pd
# Importamos tus funciones (ajusta el nombre del archivo si es necesario)
from carga_datos import cargar, convertir_a_matriz 
from recomendaciones import calculo_matriz_similitud

def probar_modulo_carga():
    print("--- INICIANDO PRUEBA DE CARGA ---")
    ruta_test = "archivos/datos_prueba.csv"
    
    # 1. Probar la función de carga
    df = cargar(ruta_test)
    
    print("\n--- VERIFICACIÓN DEL DATAFRAME ---")
    print(df)
    
    # Pasos de control (Aserciones)
    assert not df.empty, "Error: El DataFrame no debería estar vacío."
    assert "id_usuario" in df.columns, "Falta la columna usuario_id"
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
    
    print("\nTest de carga exitoso")
    print()

    matriz_similitud = calculo_matriz_similitud(matriz)
    print("Matriz similitud entre usuarios:")
    print()
    print(matriz_similitud)

if __name__ == "__main__":
    probar_modulo_carga()