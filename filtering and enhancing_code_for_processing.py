import SimpleITK as sitk
import matplotlib.pyplot as plt

# Load the 3D image
# Replace with your image path
image_path = r"E:\Backups\gfg\3D image processing in Python\final_image_incr_slice.nii.gz"
image = sitk.ReadImage(image_path)

# Gaussian smoothing
sigma = 1.0
smoothed_image = sitk.SmoothingRecursiveGaussian(image, sigma)

# Contrast enhancement using histogram equalization
enhanced_image = sitk.AdaptiveHistogramEqualization(smoothed_image)

# Convert to NumPy array
image_array = sitk.GetArrayFromImage(image)
smoothed_array = sitk.GetArrayFromImage(smoothed_image)
enhanced_array = sitk.GetArrayFromImage(enhanced_image)

# Select a slice to display
slice_index = image_array.shape[0] // 2

# Plot the original, smoothed, and enhanced images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image_array[slice_index, :, :], cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(smoothed_array[slice_index, :, :], cmap='gray')
axes[1].set_title('Smoothed Image')
axes[1].axis('off')
axes[2].imshow(enhanced_array[slice_index, :, :], cmap='gray')
axes[2].set_title('Enhanced Image')
axes[2].axis('off')
plt.show()
