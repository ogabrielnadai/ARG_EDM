from PIL import Image

l = ['27', '10', '23', '2B', '26', '2A', '28', '22', '24', '04', '29', '25']

for i in range(12):
    image_path = f'{i + 1}.png'
    image = Image.open(image_path)
    pixels = image.load()

    target_blue = int(l[i], 16)

    # matching_pixels = []
    adabadu = []
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            if b == target_blue:
                # matching_pixels.append((x, y))
                adabadu.append((r, g))

    print(f'IMAGE {i + 1}: ')
    for x in sorted(adabadu, key=lambda x: x[0]):
        print(x[1])
    print()
    print()
