import torch
import time

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print("Device:", device)

a = torch.rand(10000, 10000)
b = torch.rand(10000, 10000)

start = time.time()
_ = torch.matmul(a, b)
print("CPU time:", time.time() - start)

if torch.cuda.is_available():
    a_gpu = a.to(device)
    b_gpu = b.to(device)
    start = time.time()
    _ = torch.matmul(a_gpu, b_gpu)
    torch.cuda.synchronize()
    print("GPU time:", time.time() - start)
