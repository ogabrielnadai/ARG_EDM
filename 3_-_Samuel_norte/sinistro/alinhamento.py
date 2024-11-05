import numpy as np
import os
import csv
from PIL import Image

def calculate_shift(original_line, reference_line, max_shift):
    best_shift = 0
    best_score = float('inf')
    for shift in range(-max_shift, max_shift + 1):
        shifted_line = np.roll(original_line, shift, axis=0)
        score = np.mean(np.abs(shifted_line - reference_line))
        if score < best_score:
            best_score = score
            best_shift = shift
    return best_shift

def align_pixels_by_reference(input_image_path, reference_image_path, output_folder, csv_output_path, max_shift=1000):
    # Carregar as imagens
    img = Image.open(input_image_path)
    ref_img = Image.open(reference_image_path)
    img_array = np.array(img)
    ref_img_array = np.array(ref_img)
    
    # Verificar se as dimensões das imagens são iguais
    if img_array.shape != ref_img_array.shape:
        raise ValueError("As dimensões da imagem de entrada e da imagem de referência devem ser iguais.")
    
    # Detectar todas as linhas da imagem
    lines = list(range(img_array.shape[0]))
    
    # Criar a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Abrir o arquivo CSV para escrita
    with open(csv_output_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Line', 'Shift'])
        
        # Alinhar as linhas com base na imagem de referência
        shifted_img_array = img_array.copy()
        shifts = []
        for y in lines:
            original_line = img_array[y]
            reference_line = ref_img_array[y]
            shift = calculate_shift(original_line, reference_line, max_shift)
            shifted_img_array[y] = np.roll(original_line, shift, axis=0)
            shifts.append((y, shift))
        
        # Salvar a imagem modificada
        image_filename = 'aligned_image.png'
        shifted_img = Image.fromarray(shifted_img_array)
        shifted_img.save(os.path.join(output_folder, image_filename))
        
        # Escrever os deslocamentos no CSV
        for line, shift in shifts:
            csv_writer.writerow([line, shift])

# Exemplo de uso

align_pixels_by_reference('sinistro.png', 'output_image.png', 'output_images', 'shifts_log.csv')