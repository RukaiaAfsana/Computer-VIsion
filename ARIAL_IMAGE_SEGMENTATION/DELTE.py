import torch
DEVICE = "cuda"
test_images = torch.rand(4, 3, 256, 256).to(DEVICE)  # Random images
test_masks = torch.rand(4, 1, 256, 256).to(DEVICE)   # Random masks

logits, loss = model(test_images, test_masks)
print(f"Test loss: {loss.item()}")
