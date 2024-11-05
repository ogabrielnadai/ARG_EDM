from PIL import Image

def rolagem_infinita(imagem_entrada, imagem_saida, deslocamento=120):
    # Carregar a imagem de entrada
    img = Image.open(imagem_entrada)
    largura, altura = img.size
    
    # Criar uma nova imagem com as mesmas dimensões
    nova_img = Image.new("RGB", (largura, altura))
    
    # Processar cada pixel
    for y in range(altura):
        for x in range(largura):
            # Calcular a nova posição do pixel
            novo_x = (x + deslocamento) % largura
            nova_img.putpixel((x, y), img.getpixel((novo_x, y)))
    
    # Salvar a nova imagem
    nova_img.save(imagem_saida)

# Exemplo de uso
rolagem_infinita('saved_image.png', 'imagem_saida.png')