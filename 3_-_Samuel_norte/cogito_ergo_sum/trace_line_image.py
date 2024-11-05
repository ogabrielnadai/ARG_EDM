from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def draw_line_from_csv(image_path, csv_path, output_path):
    # Ler o arquivo CSV
    df = pd.read_csv(csv_path)
    
    # Obter as coordenadas X e Y e os valores RGB
    coordinates = list(zip(df['X'], df['Y']))
    rgb_values = list(zip(df['R'], df['G'], df['B']))
    
    # Abrir a imagem
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Desenhar a linha vermelha conectando os pontos
    #draw.line(coordinates, fill='red', width=2)
    
    # Fonte para desenhar o texto (opcional, pode ser ajustado conforme necessário)
    font = ImageFont.load_default()
    
    # Adicionar números e valores RGB em cada ponto
    for i, (x, y) in enumerate(coordinates):
        #text = f"{i+1} ({rgb_values[i][0]},{rgb_values[i][1]},{rgb_values[i][2]})"
        text = f"{i+1} ({rgb_values[i][0]},{rgb_values[i][1]},{rgb_values[i][2]})"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Ajustar a posição do texto para não ser cortado
        text_x = min(x + 5, img.width - text_width)
        text_y = max(y - text_height - 5, 0)
        
        # Desenhar um fundo para o texto
        draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], fill='black')
        
        # Desenhar o texto
        draw.text((text_x, text_y), text, fill='white', font=font)
    
    # Salvar a imagem modificada
    img.save(output_path)

# Exemplo de uso
draw_line_from_csv('bloco.png', 'sorted_by_r_output_pixels.csv', 'output_image_with_line.png')