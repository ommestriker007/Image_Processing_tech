# Image_Processing_tech
A collection of image processing and computer vision techniques applied to geospatial and remote sensing imagery using Python

# Image Processing Techniques (Geospatial Focus)

This repository contains implementations of fundamental image processing
and computer vision techniques applied to geospatial and remote sensing imagery
using Python.

## 1. Edge Detection using Sobel Filter

### Description
Edge detection is a fundamental image processing technique used to identify
boundaries and structural features in imagery. In this example, the Sobel
operator is applied to a selected spectral band of a raster image to highlight
edges.

### Dataset
- Input: GeoTIFF raster image
- Band used: Band 10 (selected for demonstration)
- Data format: Raster (GeoTIFF)

### Libraries Used
- rasterio
- scikit-image
- matplotlib

### Output
The output highlights edges in the selected band, which can be useful for:
- Feature extraction
- Structural analysis
- Pre-processing for ML models

python scripts/edge_detection_sobel.py

