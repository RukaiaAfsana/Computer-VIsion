import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from PIL import Image

import matplotlib
matplotlib.use('Agg')

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        print("Feature map shape",x.shape)
        self.visualization(x)
        x = self.relu(x)
        return x 

    def visualization(self, features):
        batch = features[0]
        num_channels = features.shape[1]
        
        for i in range(1,4):
            print(num_channels)
            plt.subplot(1, 4, i+1)
            plt.imshow(batch[i].detach().cpu(), cmap='gray')
            plt.axis('off')
        plt.show()

def load_image(img_path):
    transform = transforms.Compose([
        transforms.Resize(( 32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.5, 0.5 , 0.5],std = [0.5, 0.5, 0.5])

    ])
    image = Image.open(img_path).convert('RGB')
    image = transform(image)
    image = image.unsqueeze(0)

    return image 

    # ...existing code...

model = MyModel()
img_path = '/home/rukaia/Desktop/computer_vision/visualize_features_/sun'
input_image = load_image(img_path)
output = model(input_image)



