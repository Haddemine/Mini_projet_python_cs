import torch

data = torch.tensor([i for i in range(1, 13)])
print(data.reshape(3, 4))
print(data.reshape(2, 3, 2))

a = torch.rand(3, 1)
b = torch.rand(1, 3)
print(a + b)  # broadcasting
