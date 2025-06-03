from matplotlib import image
import torch
import numpy as np

img = image.imread("image.png")  # image RGB
tensor = torch.tensor(img / 255.0)  # Normalisation
tensor = tensor.unsqueeze(0)  # ajout de la batch dim : B x H x W x C
