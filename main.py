import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2


def generate_photon_image(original_image, photon_count):
    # Symulacja dodawania losowych fluktuacji przy użyciu rozkładu Poissona
    noisy_image = np.random.poisson(original_image * photon_count)

    # Normalizacja obrazu do zakresu [0, 255]
    normalized_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    return normalized_image


def save_image(image, filename):
    # Zapisz obraz przy użyciu OpenCV
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def main():
    # Nazwa pliku obrazu
    image_filename = "saguaro.jpg"

    # Wczytaj obraz
    original_image = np.array(Image.open(image_filename))

    # Lista różnych średnich liczby fotonów λ
    photon_counts = [1, 4, 16, 64, 256, 1024]

    # Generowanie, wyświetlanie i zapisywanie wersji obrazu dla różnych λ
    for photon_count in photon_counts:
        noisy_image = generate_photon_image(original_image, photon_count)

        plt.imshow(noisy_image)
        plt.title(f'Photon Count: {photon_count}')
        plt.show()

        # Zapisz obraz
        output_filename = f"noisy_image_{photon_count}.png"
        save_image(noisy_image, output_filename)
        print(f'Zapisano obraz jako: {output_filename}')


if __name__ == "__main__":
    main()
