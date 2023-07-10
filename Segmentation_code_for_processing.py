import SimpleITK as sitk
from skimage import segmentation
from skimage.filters import threshold_otsu
import numpy as np
import matplotlib.pyplot as plt

# Load the 3D image
# Replace with your image path
image_path = r"E:\Backups\gfg\3D image processing in Python\1-010.nii.gz"
image = sitk.ReadImage(image_path)

# Convert to NumPy array
image_array = sitk.GetArrayFromImage(image)

# Apply thresholding segmentation algorithm
threshold_value = threshold_otsu(image_array)
segmented = image_array > threshold_value

# Convert back to SimpleITK image
segmented_image = sitk.GetImageFromArray(segmented.astype(np.uint8))
segmented_image.CopyInformation(image)  # Copy the metadata from the original image

# Select a slice to display
slice_index = segmented_image.GetSize()[2] // 2
slice_image = sitk.GetArrayViewFromImage(segmented_image)[slice_index, :, :]

# Plot the original and segmented images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_array[slice_index, :, :], cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(slice_image, cmap='gray')
axes[1].set_title('Segmented Image')
axes[1].axis('off')
plt.show()

# Replace with your desired output path
output_path = r"E:\Backups\gfg\3D image processing in Python\segmented_image.nii.gz"
sitk.WriteImage(segmented_image, output_path)
