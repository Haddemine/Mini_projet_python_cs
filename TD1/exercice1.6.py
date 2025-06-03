import tensorflow as tf
import torch

tensor_tf = tf.constant([[1, 2], [3, 4]])
tensor_pt = torch.tensor([[1, 2], [3, 4]])

print("TF shape:", tensor_tf.shape)
print("PT shape:", tensor_pt.shape)
