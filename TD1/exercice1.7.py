import torch

a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Addition élément par élément:", a + b)
print("Multiplication matricielle:", torch.matmul(a, b))
print("Produit Hadamard:", a * b)
