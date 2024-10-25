from PIL import Image

data = [
    'b4 w2 b2 w4 b2 w8',
    'b2 w8       b4 w2',
    'b2 w4 b2 w8 b2 w4 b4 w2',
    'b2 w4 b4 w4 b6 w2',
    'b8 w4 b2 w2 b2 w4',
    'b2 w4 b2 w2 b4 w8',
    'b8 w2 b2 w4 b2 w4',
    'b8 w2 b2 w2 b6 w2',
    'b4 w6 b6 w2 b2 w2 b4'
]

data = [line.strip() for line in data if line.strip()]

bars = []
for line in data:
    tokens = line.strip().split()
    for token in tokens:
        color = token[0]
        width = int(token[1:])
        bars.append((color, width))

total_width = sum(width for color, width in bars)
height = 100
img = Image.new('1', (total_width, height), 1)

current_x = 0
for color, width in bars:
    if color == 'b':
        for x in range(current_x, current_x + width):
            for y in range(height):
                img.putpixel((x, y), 0)
    current_x += width
img.save('barcode.png')
