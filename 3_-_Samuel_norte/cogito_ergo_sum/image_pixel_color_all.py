from PIL import Image
import csv

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def extract_all_pixels(input_path, output_csv):
    # Abre a imagem
    img = Image.open(input_path)
    width, height = img.size
    pixels = img.load()

    # Lista para armazenar os dados dos pixels
    pixel_data = []

    # Verifica todos os pixels da imagem
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            hex_value = rgb_to_hex(r, g, b)
            pixel_data.append((x, y, r, g, b, hex_value))

    # Escreve os dados dos pixels em um arquivo CSV
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['X', 'Y', 'R', 'G', 'B', 'Hex'])
        writer.writerows(pixel_data)

# Exemplo de uso
extract_all_pixels('traco.png', 'output_pixels_all.csv')