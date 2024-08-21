# from PIL import Image
# import numpy as np
#
# def nearest_neighbor_resize(image_path, new_width=100, new_height=100):
#     # Wczytaj obraz
#     img = Image.open(image_path)
#     img_array = np.array(img)
#
#     # Oblicz skale
#     x_scale = img_array.shape[1] / new_width
#     y_scale = img_array.shape[0] / new_height
#
#     # Stwórz nowy obraz
#     new_img_array = np.zeros((new_height, new_width, img_array.shape[2]))
#
#     # Przeskaluj obraz
#     for x in range(new_width):
#         for y in range(new_height):
#             new_x = int(x * x_scale)
#             new_y = int(y * y_scale)
#             new_img_array[y, x] = img_array[new_y, new_x]
#
#     # Zapisz nowy obraz
#     new_img = Image.fromarray(new_img_array.astype('uint8'))
#     new_img.save('1024_resized_image_sasiadSas.png')
#
# # Wywołaj funkcję
# nearest_neighbor_resize('noisy_image_1024.png')
#

from PIL import Image
import numpy as np

def restore_size(image_path, original_image_path):
    # Wczytaj obraz
    img = Image.open(image_path)
    img_array = np.array(img)

    # Wczytaj oryginalny obraz
    original_img = Image.open(original_image_path)
    original_width, original_height = original_img.size

    # Oblicz skale
    x_scale = img_array.shape[1] / original_width
    y_scale = img_array.shape[0] / original_height

    # Stwórz nowy obraz
    new_img_array = np.zeros((original_height, original_width, img_array.shape[2]))

    # Przeskaluj obraz
    for x in range(original_width):
        for y in range(original_height):
            new_x = int(x * x_scale)
            new_y = int(y * y_scale)
            new_img_array[y, x] = img_array[new_y, new_x]

    # Zapisz nowy obraz
    new_img = Image.fromarray(new_img_array.astype('uint8'))
    new_img.save('1024_restored_image_sasiadLam=1024.png')

# Wywołaj funkcję
restore_size('1024_resized_image_sasiadSas.png', 'noisy_image_1024.png')
