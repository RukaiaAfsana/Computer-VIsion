import os
import shutil

# Root directory containing all folders (folder1, folder2, etc.)
root_folder = "kaggle_3m"
# Loop through each subfolder in the root directory
for subfolder in os.listdir(root_folder):
    subfolder_path = os.path.join(root_folder, subfolder)

    # Ensure it's a directory
    if os.path.isdir(subfolder_path):
        images_folder = os.path.join(subfolder_path, "images")
        masks_folder = os.path.join(subfolder_path, "masks")

        # Create images/ and masks/ subfolders if they don't exist
        os.makedirs(images_folder, exist_ok=True)
        os.makedirs(masks_folder, exist_ok=True)

        # Loop through files in the current subfolder
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)

            # Ensure it's a .tif file
            if os.path.isfile(file_path) and filename.lower().endswith(".tif"):
                if "_mask" in filename:  # If it's a mask
                    shutil.move(file_path, os.path.join(masks_folder, filename))
                    print(f"Moved {filename} to {masks_folder}")
                else:  # If it's an image
                    shutil.move(file_path, os.path.join(images_folder, filename))
                    print(f"Moved {filename} to {images_folder}")

print("Separation complete!")

