import os
import shutil

# Root directory containing all subfolders (folder1, folder2, etc.)
root_folder = "kaggle_3m"  # Change this to your actual path

# Target folders for collecting all images and masks
all_images_folder = os.path.join(root_folder, "all_images")
all_masks_folder = os.path.join(root_folder, "all_masks")

# Create target directories if they don't exist
os.makedirs(all_images_folder, exist_ok=True)
os.makedirs(all_masks_folder, exist_ok=True)

# Loop through each subfolder (folder1, folder2, etc.)
for subfolder in os.listdir(root_folder):
    subfolder_path = os.path.join(root_folder, subfolder)

    if os.path.isdir(subfolder_path):  # Ensure it's a directory
        images_folder = os.path.join(subfolder_path, "images")
        masks_folder = os.path.join(subfolder_path, "masks")

        # Move all images to the single all_images/ folder
        if os.path.isdir(images_folder):
            for filename in os.listdir(images_folder):
                src_path = os.path.join(images_folder, filename)
                dst_path = os.path.join(all_images_folder, filename)

                # Avoid overwriting by renaming duplicates
                if os.path.exists(dst_path):
                    filename = f"{subfolder}_{filename}"  # Add folder name to avoid duplicates
                    dst_path = os.path.join(all_images_folder, filename)

                shutil.move(src_path, dst_path)
                print(f"Moved {filename} to {all_images_folder}")

        # Move all masks to the single all_masks/ folder
        if os.path.isdir(masks_folder):
            for filename in os.listdir(masks_folder):
                src_path = os.path.join(masks_folder, filename)
                dst_path = os.path.join(all_masks_folder, filename)

                # Avoid overwriting by renaming duplicates
                if os.path.exists(dst_path):
                    filename = f"{subfolder}_{filename}"
                    dst_path = os.path.join(all_masks_folder, filename)

                shutil.move(src_path, dst_path)
                print(f"Moved {filename} to {all_masks_folder}")

print("All images and masks moved successfully!")

