import os
import pandas as pd

# Set the path where images and masks are stored
image_dir = "kaggle_3m/images"  # Change this to your actual image directory
mask_dir = "kaggle_3m/masks"    # Change this to your actual mask directory
csv_output = "dataset.csv"     # Output CSV file

# Get image and mask names (assuming they have the same names)
image_files = sorted(os.listdir(image_dir))  # Sort to maintain order
mask_files = sorted(os.listdir(mask_dir))    # Sort to maintain order

# Create DataFrame
df = pd.DataFrame({"images": image_files, "masks": mask_files})

# Save to CSV
df.to_csv(csv_output, index=False)

print(f"CSV file saved as {csv_output}")
