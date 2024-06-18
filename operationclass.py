import numpy as np

class IntArray:
  def __init__(self, int_array):
    if not isinstance(int_array, np.ndarray) or int_array.dtype != 'int':
      raise ValueError("Input must be a numpy array of integers")