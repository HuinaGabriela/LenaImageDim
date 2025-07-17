from PIL import Image

caminho_imagem = r'C:\Users\Administrador\Desktop\bootcamp_LLM\LenaImageDim\imagens\lena.png'

img = Image.open(caminho_imagem)
img = img.convert('RGB')  # garantir RGB

width, height = img.size

gray_pixels = []

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        gray_pixels.append(gray)

img_gray = Image.new('L', (width, height))
img_gray.putdata(gray_pixels)

threshold = 128

binary_pixels = []
for gray in gray_pixels:
    if gray > threshold:
        binary_pixels.append(255)
    else:
        binary_pixels.append(0)

img_bin = Image.new('L', (width, height))
img_bin.putdata(binary_pixels)

# Mostrar as imagens
img.show(title='Original')
img_gray.show(title='Escala de Cinza')
img_bin.show(title='Binarizada')

# Salvar
img_gray.save(r'C:\Users\Administrador\Desktop\bootcamp_LLM\LenaImageDim\imagens\lena_gray.png')
img_bin.save(r'C:\Users\Administrador\Desktop\bootcamp_LLM\LenaImageDim\imagens\lena_binary.png')
