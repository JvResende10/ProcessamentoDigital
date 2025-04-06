from PIL import Image
import numpy as np

def carregar_imagem(caminho_imagem):
    """Carrega a imagem e converte para array numpy."""
    imagem = Image.open(caminho_imagem)
    return np.array(imagem)

def contar_pixels(imagem_array, codigo):
    """Conta pixels com um determinado código na imagem."""
    return np.sum(imagem_array == codigo)

def calcular_area_hectares(pixels_classe, pixels_validos, area_total_hectares):
    """Calcula a área em hectares para uma classe específica."""
    return (pixels_classe / pixels_validos) * area_total_hectares

def processar_imagem(caminho_imagem, area_brasil_hectares=851576700.0):
    """Processa a imagem e retorna as estatísticas."""
    imagem_array = carregar_imagem(caminho_imagem)
    total_pixels = imagem_array.size
    
    pixels_sem_dados = contar_pixels(imagem_array, 0)
    pixels_soja = contar_pixels(imagem_array, 39)
    pixels_pastagem = contar_pixels(imagem_array, 15)
    
    pixels_validos = total_pixels - pixels_sem_dados
    
    area_soja = calcular_area_hectares(pixels_soja, pixels_validos, area_brasil_hectares)
    area_pastagem = calcular_area_hectares(pixels_pastagem, pixels_validos, area_brasil_hectares)
    
    return {
        'total_pixels': total_pixels,
        'pixels_sem_dados': pixels_sem_dados,
        'pixels_soja': pixels_soja,
        'pixels_pastagem': pixels_pastagem,
        'area_soja': area_soja,
        'area_pastagem': area_pastagem
    }

if __name__ == "__main__":
    # Exemplo de uso
    caminho_imagem = "Coloque aqui o path da imagem"
    resultados = processar_imagem(caminho_imagem)
    
    print(f"Total de pixels: {resultados['total_pixels']}")
    print(f"Pixels sem dados (código 0): {resultados['pixels_sem_dados']}")
    print(f"Pixels de soja (código 39): {resultados['pixels_soja']}")
    print(f"Pixels de pastagem (código 15): {resultados['pixels_pastagem']}")
    print(f"Área de plantio de soja: {resultados['area_soja']:.2f} hectares")
    print(f"Área de cobertura de pastagem: {resultados['area_pastagem']:.2f} hectares")
