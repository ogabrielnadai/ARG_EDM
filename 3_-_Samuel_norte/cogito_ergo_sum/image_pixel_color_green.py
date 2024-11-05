from PIL import Image
import csv

def is_near_green(r, g, b, threshold=50):
    # Define a cor verde como (0, 255, 0)
    green = (0, 255, 0)
    return abs(r - green[0]) < threshold and abs(g - green[1]) < threshold and abs(b - green[2]) < threshold

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def extract_green_pixels(input_path, output_csv):
    # Abre a imagem
    img = Image.open(input_path)
    width, height = img.size
    pixels = img.load()

    # Define a margem de 150 pixels
    margin = 150

    # Lista para armazenar os dados dos pixels
    pixel_data = []

    # Verifica os pixels nas bordas com a margem
    for x in range(width):
        for y in range(height):
            if x < margin or x >= width - margin or y < margin or y >= height - margin:
                r, g, b = pixels[x, y]
                if is_near_green(r, g, b):
                    hex_value = rgb_to_hex(r, g, b)
                    pixel_data.append((x, y, r, g, b, hex_value))

    # Escreve os dados dos pixels em um arquivo CSV
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['X', 'Y', 'R', 'G', 'B', 'Hex'])
        writer.writerows(pixel_data)

# Exemplo de uso
extract_green_pixels('bloco.png', 'output_pixels.csv')