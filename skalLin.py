import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def linear_interpolation(image, new_size):
    height, width = image.shape[:2]
    new_height, new_width = new_size

    # Współczynniki skalowania w pionie i poziomie
    scale_y = new_height / height
    scale_x = new_width / width

    # Nowy obraz
    new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            # Współrzędne piksela w oryginalnym obrazie
            original_i = i / scale_y
            original_j = j / scale_x

            # Koordynaty pikseli sąsiadujących
            top_i, bottom_i = int(np.floor(original_i)), int(np.ceil(original_i))
            left_j, right_j = int(np.floor(original_j)), int(np.ceil(original_j))

            # Wagi dla pikseli sąsiadujących
            weight_top = bottom_i - original_i
            weight_bottom = original_i - top_i
            weight_left = right_j - original_j
            weight_right = original_j - left_j

            # Interpolacja liniowa
            new_image[i, j, :] = (
                weight_right * (weight_bottom * image[top_i, left_j, :] + weight_top * image[bottom_i, left_j, :]) +
                weight_left * (weight_bottom * image[top_i, right_j, :] + weight_top * image[bottom_i, right_j, :])
            ).astype(np.uint8)

    return new_image

def save_image(image, filename):
    # Zapisz obraz przy użyciu OpenCV
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

def main():
    # Nazwa pliku obrazu
    image_filename = "noisy_image_1.png"

    # Wczytaj obraz
    original_image = np.array(Image.open(image_filename))

    # Przeskaluj obraz do rozmiaru 100x100 przy użyciu interpolacji liniowej
    new_size = (100, 100)
    scaled_image = linear_interpolation(original_image, new_size)

    # Wyświetl oryginalny i przeskalowany obraz
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('Oryginalny obraz')

    plt.subplot(1, 2, 2)
    plt.imshow(scaled_image)
    plt.title('Przeskalowany obraz (interpolacja liniowa)')

    plt.show()

    # Zapisz przeskalowany obraz
    output_filename = "przeskalowany_obraz_interpolacja_liniowa.png"
    save_image(scaled_image, output_filename)
    print(f'Zapisano przeskalowany obraz jako: {output_filename}')

if __name__ == "__main__":
    main()
