import SimpleITK as sitk

# Load the 3D image
# Replace with your image path
image_path = r"E:\Backups\gfg\3D image processing in Python\final_image_incr_slice.nii.gz"
image = sitk.ReadImage(image_path)

# Get the size of the image
size = image.GetSize()
num_slices = size[2]

print(f"The number of slices in the image is: {num_slices}")
