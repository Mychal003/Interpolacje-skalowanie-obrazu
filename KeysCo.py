# from PIL import Image
# import numpy as np
# import scipy.ndimage
#
# def keys_interpolation_resize(image_path, new_width=100, new_height=100):
#     # Wczytaj obraz
#     img = Image.open(image_path)
#     img_array = np.array(img)
#
#     # Przeskaluj obraz
#     new_img_array = scipy.ndimage.zoom(img_array, (new_height/img_array.shape[0], new_width/img_array.shape[1], 1))
#
#     # Zapisz nowy obraz
#     new_img = Image.fromarray(new_img_array.astype('uint8'))
#     new_img.save('1024_resized_image_KeysLam=1024.png')
#
# # Wywołaj funkcję
# keys_interpolation_resize('noisy_image_1024.png')

from PIL import Image
import numpy as np
import scipy.ndimage

def restore_size(image_path, original_image_path):
    # Wczytaj obraz
    img = Image.open(image_path)
    img_array = np.array(img)

    # Wczytaj oryginalny obraz
    original_img = Image.open(original_image_path)
    original_width, original_height = original_img.size

    # Przeskaluj obraz
    new_img_array = scipy.ndimage.zoom(img_array, (original_height/img_array.shape[0], original_width/img_array.shape[1], 1))

    # Zapisz nowy obraz
    new_img = Image.fromarray(new_img_array.astype('uint8'))
    new_img.save('1024_restored_image-KeysLam=1024.png')

# Wywołaj funkcję
restore_size('1024_resized_image_KeysLam=1024.png', 'noisy_image_1024.png')
