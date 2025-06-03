import tensorflow as tf
import torch

# TF → PT
tf_tensor = tf.constant([[1, 2], [3, 4]])
pt_tensor = torch.tensor(tf_tensor.numpy())

# PT → TF
tf_tensor2 = tf.convert_to_tensor(pt_tensor.numpy())
