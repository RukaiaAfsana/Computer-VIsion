import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the images
base_url = "https://www.cs.toronto.edu/~vmnih/data/mass_roads/train/map/index.html"

# Create the 'train_mask' directory to save images
os.makedirs("train_mask", exist_ok=True)

# Get the HTML content
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Loop through all links and download images
for link in soup.find_all("a"):
    file_name = link.get("href")
    
    # Check if the link is a valid image file (e.g., .jpg, .png, .tif)
    if file_name.endswith((".jpg", ".png", ".tif")):
        # Join the base URL with the file name to form the full URL
        img_url = urljoin(base_url, file_name)
        
        # Extract the actual file name (remove the path portion)
        actual_file_name = os.path.basename(file_name)
        
        # Stop downloading when reaching "20278945_15.tif"
        if actual_file_name == "20278945_15.tif":
            print(f"Reached {actual_file_name}, stopping download.")
            break  # Exit the loop
        
        # Get the image data
        img_data = requests.get(img_url).content
        
        # Save the image in the 'train_named' folder
        with open(f"train_mask/{actual_file_name}", "wb") as img_file:
            img_file.write(img_data)
        print(f"Downloaded: {actual_file_name}")

print("Download complete up to 20278945_15.tif!")
