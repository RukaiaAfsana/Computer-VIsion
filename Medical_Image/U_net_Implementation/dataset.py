import numpy as np 
from PIL import Image
import os
from torch.utils.data import Dataset


class Dataset_A(Dataset):
    def __init__(self,image_dir,mask_dir,transform= None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir) ##list all the images in this directory
        print(self.images)


    def __len__(self):
        return len(self.images)


    def __getitem__(self, index):
        img_path = os.path.join(self.image_dir,self.images[index])
        mask_path = os.path.join(self.mask_dir,self.images[index])
        image = np.array(Image.open(img_path).convert("RGB"))
        mask = np.array(Image.open(mask_path).convert("L"),dtype=np.float32)
        mask[mask == 255.0] = 1.0 ###normalize the mask values, 255 is used to represent the foreground, 0 is background

        if self.transform is not  None:
            augmentations = self.transform(image= image,mask = mask)
            image = augmentations["image"]
            mask = augmentations["masks"]

        return image, mask
if __name__=="__main__":
    D = Dataset_A("/home/rukaia/Desktop/computer_vision/medical_imaging_/data/colon/image","/home/rukaia/Desktop/computer_vision/medical_imaging_/data/colon/mask")
