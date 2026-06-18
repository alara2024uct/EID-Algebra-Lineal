import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def calculo_matriz_similitud(matriz_usuario_producto: pd.DataFrame) -> pd.DataFrame:

    print("Calculando matriz similitud")

    valores_matriz = cosine_similarity(matriz_usuario_producto)

    usuarios = matriz_usuario_producto.index
    matriz_similitud = pd.DataFrame(valores_matriz, index = usuarios, columns = usuarios)

    print(f"matriz: {matriz_similitud.shape}")
    return matriz_similitud
