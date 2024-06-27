import numpy as np
from operationclass import IntArray

def productivity_of_company(order, data_frame):
  return np.sum(data_frame[order])


# Function to find the company with the highest productivity
def max_productivity(data_frame):
  i = 0
  best_company = i + 1
  num_of_products = 0

  for i in range(len(data_frame)):
    result = productivity_of_company(i, data_frame)
    if result > num_of_products:
      num_of_products = result
      best_company = i + 1
  print(f"Company {best_company} is the best with {num_of_products} products")    




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