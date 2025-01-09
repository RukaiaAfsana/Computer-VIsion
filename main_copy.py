import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
class ImageModel(nn.Module):
    def __init__(self):
        super(ImageModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        print("Feature map shape:", x.shape)
        self.visualize_features(x)  # Visualize feature maps
        x = self.relu(x)
        return x

    def visualize_features(self, features):
        # Visualize feature maps (first sample in the batch)
        num_channels = features.shape[1]
        batch = features[0] 
        num_channels = batch.shape[0]
        grid_size = int(num_channels**0.5)
         # First image in the batch
        for i in range(num_channels):  # Visualize up to 4 channels
            plt.subplot(grid_size,grid_size, i + 1)
            plt.imshow(batch[i].detach().cpu(), cmap='gray')
            plt.title(f"Channel {i+1}")
            plt.axis('off')
        plt.show(block=True)
        plt.savefig('output_plot.png')

# Load and preprocess the image
def load_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),        # Resize to 32x32
        transforms.ToTensor(),             # Convert to Tensor (C, H, W)
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normalize
    ])
    image = Image.open(image_path).convert('RGB')  # Open and ensure RGB
    image = transform(image)  # Apply transformations
    image = image.unsqueeze(0)  # Add batch dimension (1, C, H, W)
    return image

# Create model instance
model = ImageModel()

# Path to the actual image
image_path1 = "/home/rukaia/Desktop/computer_vision/visualize_features_/sun"
image_path2 = "/home/rukaia/Desktop/computer_vision/visualize_features_/bird.jpeg"
image_path3 = "/home/rukaia/Desktop/computer_vision/visualize_features_/road.jpg"  # Replace with your image path
input_image1 = load_image(image_path1)
input_image2 = load_image(image_path2)
input_image3 = load_image(image_path3)
batch_input = torch.cat([input_image1, input_image2, input_image3], dim=0)
model.eval()
# Forward pass through the model
output = model(batch_input)
