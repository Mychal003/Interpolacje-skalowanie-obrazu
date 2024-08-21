import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.interpolate import RegularGridInterpolator
import cv2

def bicubic_interpolation(image, new_size):
    height, width = image.shape[:2]
    new_height, new_width = new_size

    # Współczynniki skalowania w pionie i poziomie
    scale_y = new_height / height
    scale_x = new_width / width

    # Współrzędne nowego obrazu
    new_y, new_x = np.mgrid[0:new_height:1, 0:new_width:1]

    # Współrzędne oryginalnego obrazu
    original_y, original_x = new_y / scale_y, new_x / scale_x

    # Przygotowanie punktów i wartości do interpolacji dwusześciennej
    points = (np.arange(height), np.arange(width))
    values = image.transpose(2, 0, 1).reshape((3, height, width))

    # Interpolacja dwusześcieniowa
    interpolator = RegularGridInterpolator(points, values, method='cubic', bounds_error=False, fill_value=0)
    interpolated_image = interpolator((original_y, original_x)).reshape((3, new_height, new_width)).transpose(1, 2, 0)

    return interpolated_image.astype(np.uint8)

def save_image(image, filename):
    # Zapisz obraz przy użyciu OpenCV
    cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

def main():
    # Nazwa pliku obrazu
    image_filename = "noisy_image_1.png"

    # Wczytaj obraz
    original_image = np.array(Image.open(image_filename))

    # Przeskaluj obraz do rozmiaru 100x100 przy użyciu interpolacji dwusześciennej
    new_size = (100, 100)
    scaled_image = bicubic_interpolation(original_image, new_size)

    # Wyświetl oryginalny i przeskalowany obraz
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('Oryginalny obraz')

    plt.subplot(1, 2, 2)
    plt.imshow(scaled_image)
    plt.title('Przeskalowany obraz (interpolacja dwusześcieniowa)')

    plt.show()

    # Zapisz przeskalowany obraz
    output_filename = "przeskalowany_obraz_interpolacja_dwusześcieniowa.png"
    save_image(scaled_image, output_filename)
    print(f'Zapisano przeskalowany obraz jako: {output_filename}')

if __name__ == "__main__":
    main()
