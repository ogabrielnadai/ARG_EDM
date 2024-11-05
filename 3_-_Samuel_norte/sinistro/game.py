import cv2
import numpy as np

# Carrega a imagem
image = cv2.imread('solve.png')
if image is None:
    print("Erro ao carregar a imagem.")
    exit()

# Variáveis de controle
zoom_level = 1.0  # Nível de zoom
line_offsets = [0] * image.shape[0]  # Deslocamento de linhas
selected_line = 0

# Cor da linha selecionada e da linha de destaque
highlight_color = (0, 255, 0)  # Verde
selection_color = (255, 0, 0)  # Azul

# Função para desenhar uma linha na imagem
def draw_line(image, line_index, line_offset, zoom_level):
    height, width = image.shape[:2]
    if 0 <= line_index < height:
        # Cálculo das coordenadas com zoom
        scaled_line_index = int(line_index * zoom_level)

        # Desenho da linha de destaque
        cv2.line(image, (line_offset, scaled_line_index), (line_offset, scaled_line_index), highlight_color, 2)  # Linha selecionada
        cv2.line(image, (line_offset - 1, scaled_line_index), (line_offset - 1, scaled_line_index), selection_color, 1)  # Linha de destaque

# Função para aplicar zoom na imagem
def apply_zoom(image, zoom_level):
    height, width = image.shape[:2]
    scaled_image = cv2.resize(image, None, fx=zoom_level, fy=zoom_level, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Função para aplicar o deslocamento da linha
def shift_line(original_image, line_index, offset):
    height, width, channels = original_image.shape
    if 0 <= line_index < height:
        # Desloca a linha selecionada para cada canal individualmente
        for c in range(channels):
            line = original_image[line_index, :, c].copy()
            shifted_line = np.roll(line, offset)  # Empurra a linha para a esquerda ou direita
            original_image[line_index, :, c] = shifted_line
        # Corrige o deslocamento para que seja aplicado corretamente
        line_offsets[line_index] = (line_offsets[line_index] + offset) % width  # Salva o deslocamento

def save_image(image, filename='saved_image.png'):
    cv2.imwrite(filename, image)
    print(f"Imagem salva como {filename}")

while True:
    # Cria uma cópia da imagem original para desenhar
    display_image = image.copy()

    # Aplica zoom na imagem
    zoomed_image = apply_zoom(display_image, zoom_level)

    # Desenha a linha selecionada
    draw_line(zoomed_image, selected_line, line_offsets[selected_line], zoom_level)

    # Exibe a imagem
    cv2.imshow('Manipulação de Linhas da Imagem', zoomed_image)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Sair com 'q'
        break
    elif key == ord('w'):  # Move para cima
        selected_line = (selected_line - 1) % image.shape[0]
    elif key == ord('s'):  # Move para baixo
        selected_line = (selected_line + 1) % image.shape[0]
    elif key == ord('a'):  # Empurra para a esquerda
        shift_line(image, selected_line, -1)
    elif key == ord('d'):  # Empurra para a direita
        shift_line(image, selected_line, 1)
    elif key == ord('+'):  # Zoom in
        zoom_level += 0.1
    elif key == ord('-'):  # Zoom out
        zoom_level = max(0.1, zoom_level - 0.1)  # Limite mínimo para zoom
    elif key == ord('k'):  # Salvar imagem
        save_image(zoomed_image)  # Salva a imagem atual

# Encerra a janela
cv2.destroyAllWindows()