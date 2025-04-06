import pytest
import numpy as np
from Processamento import contar_pixels, calcular_area_hectares, processar_imagem

def test_contar_pixels():
    # Criar uma imagem de teste com valores conhecidos
    imagem_teste = np.array([
        [0, 39, 15],
        [39, 0, 39],
        [15, 15, 0]
    ])
    
    assert contar_pixels(imagem_teste, 0) == 3
    assert contar_pixels(imagem_teste, 39) == 3
    assert contar_pixels(imagem_teste, 15) == 3

def test_calcular_area_hectares():
    # Teste com valores conhecidos
    pixels_classe = 100
    pixels_validos = 1000
    area_total = 1000
    
    area = calcular_area_hectares(pixels_classe, pixels_validos, area_total)
    assert area == 100  # (100/1000) * 1000 = 100

def test_processar_imagem(tmp_path):
    # Criar uma imagem de teste
    imagem_teste = np.array([
        [0, 39, 15],
        [39, 0, 39],
        [15, 15, 0]
    ])
    
    # Salvar a imagem de teste
    import os
    from PIL import Image
    caminho_imagem = os.path.join(tmp_path, "teste.png")
    Image.fromarray(imagem_teste.astype(np.uint8)).save(caminho_imagem)
    
    # Processar a imagem
    resultados = processar_imagem(caminho_imagem, area_brasil_hectares=1000)
    
    assert resultados['total_pixels'] == 9
    assert resultados['pixels_sem_dados'] == 3
    assert resultados['pixels_soja'] == 3
    assert resultados['pixels_pastagem'] == 3
    assert resultados['area_soja'] == 500  # (3/6) * 1000
    assert resultados['area_pastagem'] == 500  # (3/6) * 1000 