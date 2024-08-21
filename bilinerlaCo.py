# from PIL import Image
# import numpy as np
#
# def bilinear_interpolation_resize(image_path, new_width=100, new_height=100):
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
#             x1 = int(x * x_scale)
#             y1 = int(y * y_scale)
#             x2 = min(x1 + 1, img_array.shape[1] - 1)
#             y2 = min(y1 + 1, img_array.shape[0] - 1)
#
#             # Oblicz wartości dla interpolacji
#             q11 = img_array[y1, x1]
#             q12 = img_array[y2, x1]
#             q21 = img_array[y1, x2]
#             q22 = img_array[y2, x2]
#
#             # Oblicz współczynniki dla interpolacji
#             x_frac = (x * x_scale) - x1
#             y_frac = (y * y_scale) - y1
#
#             # Wykonaj interpolację
#             new_img_array[y, x] = (q11 * (1 - x_frac) * (1 - y_frac) +
#                                    q21 * x_frac * (1 - y_frac) +
#                                    q12 * (1 - x_frac) * y_frac +
#                                    q22 * x_frac * y_frac)
#
#     # Zapisz nowy obraz
#     new_img = Image.fromarray(new_img_array.astype('uint8'))
#     new_img.save('1024_resized_image-bilin_lam=1024.png')
#
# # Wywołaj funkcję
# bilinear_interpolation_resize('noisy_image_1024.png')

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
            x1 = int(x * x_scale)
            y1 = int(y * y_scale)
            x2 = min(x1 + 1, img_array.shape[1] - 1)
            y2 = min(y1 + 1, img_array.shape[0] - 1)

            # Oblicz wartości dla interpolacji
            q11 = img_array[y1, x1]
            q12 = img_array[y2, x1]
            q21 = img_array[y1, x2]
            q22 = img_array[y2, x2]

            # Oblicz współczynniki dla interpolacji
            x_frac = (x * x_scale) - x1
            y_frac = (y * y_scale) - y1

            # Wykonaj interpolację
            new_img_array[y, x] = (q11 * (1 - x_frac) * (1 - y_frac) +
                                   q21 * x_frac * (1 - y_frac) +
                                   q12 * (1 - x_frac) * y_frac +
                                   q22 * x_frac * y_frac)

    # Zapisz nowy obraz
    new_img = Image.fromarray(new_img_array.astype('uint8'))
    new_img.save('1024_restored_image_bilinLam=1024.png')

# Wywołaj funkcję
restore_size('1024_resized_image-bilin_lam=1024.png', 'noisy_image_1024.png')
