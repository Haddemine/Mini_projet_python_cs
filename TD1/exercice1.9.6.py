import torch
import torch.nn.init as init

zeros = torch.zeros(3, 3)
uniform = torch.empty(3, 3).uniform_(0, 1)
normal = torch.empty(3, 3).normal_(0, 1)
xavier = torch.empty(3, 3)
init.xavier_uniform_(xavier)
