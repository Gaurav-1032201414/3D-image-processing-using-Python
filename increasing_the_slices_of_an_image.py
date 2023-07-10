import SimpleITK as sitk

# Load the 3D image
# Replace with your image path
image_path = r"E:\Backups\gfg\3D image processing in Python\1-010.nii.gz"
image = sitk.ReadImage(image_path)

# Get the original size and spacing of the image
original_size = image.GetSize()
original_spacing = image.GetSpacing()

# Define the desired spacing and number of slices
desired_spacing = (original_spacing[0], original_spacing[1], 2.0)  # New spacing in z-dimension
desired_num_slices = 50  # New number of slices

# Calculate the new size based on the desired spacing and number of slices
new_size = (
    original_size[0],
    original_size[1],
    int(original_size[2] * original_spacing[2] / desired_spacing[2] * desired_num_slices)
)

# Perform resampling to increase the number of slices
resampler = sitk.ResampleImageFilter()
resampler.SetSize(new_size)
resampler.SetOutputSpacing(desired_spacing)
resampler.SetOutputOrigin(image.GetOrigin())
resampler.SetOutputDirection(image.GetDirection())
resampled_image = resampler.Execute(image)


# Save the resampled image
output_path = r"final_image_incr_slice.nii.gz"  # Replace with your desired output path
sitk.WriteImage(resampled_image, output_path)




