from PIL import Image
import numpy as np

imagem = Image.open(
    "Coloque aqui o path da imagem"
)
imagem_array = np.array(imagem)


def contar_pixels(codigo):
    return np.sum(imagem_array == codigo)


total_pixels = imagem_array.size

pixels_sem_dados = contar_pixels(0)

pixels_soja = contar_pixels(39)

pixels_pastagem = contar_pixels(15)

area_brasil_hectares = 851576700.0

pixels_validos = total_pixels - pixels_sem_dados

area_soja_hectares = (pixels_soja / pixels_validos) * area_brasil_hectares
area_pastagem_hectares = (pixels_pastagem / pixels_validos) * area_brasil_hectares

print(f"Total de pixels: {total_pixels}")
print(f"Pixels sem dados (código 0): {pixels_sem_dados}")
print(f"Pixels de soja (código 39): {pixels_soja}")
print(f"Pixels de pastagem (código 15): {pixels_pastagem}")
print(f"Área de plantio de soja: {area_soja_hectares:.2f} hectares")
print(f"Área de cobertura de pastagem: {area_pastagem_hectares:.2f} hectares")
