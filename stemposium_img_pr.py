import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from skimage.data import camera  # Sample image
from skimage.color import rgb2gray
from skimage.transform import resize

# Load and preprocess the image
image = camera()  # Load a sample grayscale image
image = resize(image, (256, 256))  # Resize for faster computation
image = image / np.max(image)  # Normalize

# Compute the 2D Fourier transform
F_image = np.fft.fftshift(np.fft.fft2(image))
magnitude_spectrum = np.log(np.abs(F_image) + 1)

# Function to reconstruct the image progressively
def reconstruct_image(F, percentage):
    rows, cols = F.shape
    mask = np.zeros_like(F, dtype=bool)
    center_x, center_y = rows // 2, cols // 2
    max_radius = min(center_x, center_y)
    radius = int(max_radius * percentage)

    for i in range(rows):
        for j in range(cols):
            if np.sqrt((i - center_x)**2 + (j - center_y)**2) < radius:
                mask[i, j] = True

    F_masked = F * mask
    return np.abs(np.fft.ifft2(np.fft.ifftshift(F_masked)))

# Set up the figure and axes
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(magnitude_spectrum, cmap='hot')
ax[1].set_title('Fourier Spectrum')
ax[1].axis('off')

reconstructed = ax[2].imshow(np.zeros_like(image), cmap='gray', vmin=0, vmax=1)
ax[2].set_title('Reconstructed Image')
ax[2].axis('off')

# Animation function
percentages = np.linspace(0.01, 1.0, 100)

def update(frame):
    perc = percentages[frame]
    reconstructed_image = reconstruct_image(F_image, perc)
    reconstructed.set_data(reconstructed_image)
    ax[2].set_title(f'Reconstructed Image ({int(perc * 100)}%)')
    return reconstructed,

# Animate
ani = FuncAnimation(fig, update, frames=len(percentages), interval=50, blit=True)

plt.tight_layout()
plt.show()
