import rasterio
from skimage.filters import sobel
import matplotlib.pyplot as plt

# Path to input image
image_path = "C:\Users\ieomk\OneDrive\Documents\Bharti_Vidypeeth\mining_analysis_pipeline\data\input\merged.tif"

with rasterio.open(image_path) as src:
    image = src.read(10)  # Selecting band 10 for edge detection

# Apply Sobel edge detection
edges = sobel(image)

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(image, cmap="gray")
axes[0].set_title("Original Band 10")
axes[0].axis("off")

axes[1].imshow(edges, cmap="gray")
axes[1].set_title("Edge Detection (Sobel)")
axes[1].axis("off")

plt.tight_layout()
plt.show()
