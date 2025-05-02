# Aerial Road Segmentation using U-Net

This project focuses on semantic segmentation of aerial imagery to detect and segment road networks from high-resolution satellite images. The goal is to automate the extraction of road masks from raw aerial data using deep learning techniques.

We used a U-Net architecture implemented via the [`segmentation_models.pytorch`](https://github.com/qubvel/segmentation_models.pytorch) library, which provides high-level building blocks for state-of-the-art segmentation models in PyTorch. U-Net is a popular encoder-decoder architecture widely used in biomedical and remote sensing image segmentation tasks due to its strong localization capabilities.

The dataset used is a subset of the **Massachusetts Roads Dataset**, which contains aerial images of the state of Massachusetts along with binary road masks. The model is trained to predict a binary segmentation mask that accurately highlights the road areas in the input image.

This project includes:
- Preprocessing pipeline for input images and masks
- U-Net model training using PyTorch
- Inference and visualization of predicted masks
- Evaluation using common metrics such as IoU and Dice coefficient
