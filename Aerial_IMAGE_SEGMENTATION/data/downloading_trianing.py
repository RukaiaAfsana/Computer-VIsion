import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Base URL of the images
base_url = "https://www.cs.toronto.edu/~vmnih/data/mass_roads/train/sat/"

# Create the 'train_named' directory to save images
os.makedirs("train_named", exist_ok=True)

# Get the HTML content
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Loop through all links and download images
for link in soup.find_all("a"):
    file_name = link.get("href")
    
    # Check if the link is a valid image file (e.g., .jpg, .png, .tiff)
    if file_name.endswith((".jpg", ".png", ".tiff")):
        # Join the base URL with the file name to form the full URL
        img_url = urljoin(base_url, file_name)
        
        # Extract the actual file name (remove the path portion)
        actual_file_name = os.path.basename(file_name)
        
        # Get the image data
        img_data = requests.get(img_url).content
        
        # Save the image in the 'train_named' folder
        with open(f"train_named/{actual_file_name}", "wb") as img_file:
            img_file.write(img_data)
        print(f"Downloaded: {actual_file_name}")

print("All images downloaded and saved in 'train_named' folder!")
