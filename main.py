import numpy as np


def file_handling():
  #open the file in read mode
  lines = []
  with open('company.txt','r') as file:
    for line in file:
      values = line.strip().split(',')
      int_values = [int(val) for val in values]
      lines.append(int_values)
      
    data_frame = np.array([np.array(row) for row in lines], dtype='object')
    return data_frame  
    
    