import cv2
import numpy as np

# Read the image
image = cv2.imread('snake.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("snake.jpg not found. Ensure the image is in the working directory.")

# Apply Fourier Transform
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Create a mask for low-pass filtering
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Center
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

# Apply mask and inverse DFT
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Normalize to displayable format
processed_image = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
processed_image = np.uint8(processed_image)

# Save the processed image
cv2.imwrite('processed_snake.jpg', processed_image)
print("Processed image saved as 'processed_snake.jpg'")
