import torch

seq = [1, 3, 5, 7, 9, 11]
X = [seq[i:i+2] for i in range(len(seq)-3)]
y = [seq[i+2:i+3] for i in range(len(seq)-3)]

X = torch.tensor(X)
y = torch.tensor(y)
