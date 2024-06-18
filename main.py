import numpy as np


def file_handling():
  #open the file in read mode
  lines = []
  with open('company.txt','r') as file:
    for line in file:
      values = line.strip().split(',')
      int_values = [int(val) for val in values]
      lines.append(int_values)