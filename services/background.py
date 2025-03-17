# from PIL import Image
# from rembg import remove
#
#
# def process_image(image_path: str, mode: str = 'mono', color: tuple | None = (255, 255, 255)):
#     with open(image_path, 'rb') as f:
#         image = f.read()
#     image_nobg = remove(image)
#
#     tmp_path = image_path + '_nobg.png'
#     with open(tmp_path, 'wb') as f:
#         f.write(image_nobg)
#
#     foreground = Image.open(tmp_path).convert('RGBA')
#
#     if mode == 'mono':
#         background = Image.new('RGBA', foreground.size, color)
#         img = Image.alpha_composite(background, foreground)
#     else:
#         img = None
#         # img = Image.alpha_composite(foreground, background)
#
#     result_path = image_path + '_processed.png'
#     img.save(result_path)
#
#     return result_path

from PIL import Image
from rembg import remove

def process_image(image_path: str, color: tuple | None = (255, 255, 255)):
    with open(image_path, 'rb') as f:
        image = f.read()
    image_nobg = remove(image)

    tmp_path = image_path + '_nobg.png'
    with open(tmp_path, 'wb') as f:
        f.write(image_nobg)

    foreground = Image.open(tmp_path).convert('RGBA')

    background = Image.new('RGBA', foreground.size, color)
    img = Image.alpha_composite(background, foreground)

    result_path = image_path + '_processed.png'
    img.save(result_path)

    return result_path

def process_image_with_custom_background(image_path: str, background_path: str):
    with open(image_path, 'rb') as f:
        image = f.read()
    image_nobg = remove(image)

    tmp_path = image_path + '_nobg.png'
    with open(tmp_path, 'wb') as f:
        f.write(image_nobg)

    foreground = Image.open(tmp_path).convert('RGBA')

    background = Image.open(background_path).convert('RGBA')
    background = background.resize(foreground.size)

    img = Image.alpha_composite(background, foreground)

    result_path = image_path + '_processed_custom.png'
    img.save(result_path)

    return result_path

