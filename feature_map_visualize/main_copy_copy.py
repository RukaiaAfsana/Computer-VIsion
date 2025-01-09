import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
plt.ion()
import matplotlib
matplotlib.use('TkAgg')
# Step 1: Define a simple CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1, padding=1)  # 3 input channels (RGB), 8 filters

    def forward(self, x):
        return self.conv1(x)  # Pass through the convolutional layer

# Step 2: Preprocess images
def load_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize to a fixed size
        transforms.ToTensor(),         # Convert to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize for pretrained models
    ])
    image = Image.open(image_path).convert("RGB")  # Ensure 3-channel RGB
    return transform(image).unsqueeze(0)  # Add batch dimension

# Paths to images
image_paths = [
    "/home/rukaia/Desktop/computer_vision/visualize_features_/sun",
    "/home/rukaia/Desktop/computer_vision/visualize_features_/bird.jpeg",
    "/home/rukaia/Desktop/computer_vision/visualize_features_/road.jpg"
]

# Load images and combine into a batch
images = [load_image(path) for path in image_paths]
batch_input = torch.cat(images, dim=0)  # Shape: (3, 3, 224, 224)

# Step 3: Create the model and process the images
model = SimpleCNN()
model.eval()  # Set to evaluation mode
feature_maps = model(batch_input)  # Shape: (3, 8, 224, 224)

# Step 4: Visualize the feature maps
def visualize_feature_maps(feature_maps, num_images=3):
    batch_size, num_channels, height, width = feature_maps.shape
    for img_idx in range(num_images):  # Iterate over images
        plt.figure(figsize=(15, 15))
        for channel_idx in range(min(num_channels, 8)):  # Display first 8 channels
            plt.subplot(2, 4, channel_idx + 1)  # Arrange in a 2x4 grid
            plt.imshow(feature_maps[img_idx, channel_idx].detach().cpu(), cmap='gray')
            plt.title(f"Image {img_idx + 1} - Channel {channel_idx + 1}")
            plt.axis('off')
        plt.show(block=True)

# Visualize feature maps for the first 8 channels
visualize_feature_maps(feature_maps)
