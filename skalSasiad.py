import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def nearest_neighbor_interpolation(image, new_size):
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
            original_i = int(i / scale_y)
            original_j = int(j / scale_x)

            # Ustawienie wartości piksela w nowym obrazie na wartość najbliższego sąsiada
            new_image[i, j, :] = image[original_i, original_j, :]

    return new_image

def save_image(image, filename):
    # Zapisz obraz przy użyciu OpenCV
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

def main():
    # Nazwa pliku obrazu
    image_filename = "noisy_image_1.png"

    # Wczytaj obraz
    original_image = np.array(Image.open(image_filename))

    # Przeskaluj obraz do rozmiaru 100x100
    new_size = (100, 100)
    scaled_image = nearest_neighbor_interpolation(original_image, new_size)

    # Wyświetl oryginalny i przeskalowany obraz
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('Oryginalny obraz')

    plt.subplot(1, 2, 2)
    plt.imshow(scaled_image)
    plt.title('Przeskalowany obraz (najbliższy sąsiad)')

    plt.show()

    # Zapisz przeskalowany obraz
    output_filename = "przeskalowany_obraz_sasiad.png"
    save_image(scaled_image, output_filename)
    print(f'Zapisano przeskalowany obraz jako: {output_filename}')

if __name__ == "__main__":
    main()
