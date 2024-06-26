import numpy as np
from operationclass import IntArray

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

def main():
  data_frame = file_handling()
  print(data_frame)

  first_branch = IntArray(data_frame[0])
  first_branch.display()
  first_branch.salary()
  first_branch.show_data()
  
main()