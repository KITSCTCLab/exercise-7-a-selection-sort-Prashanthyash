from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for step in range(size):
    min-idx= step
    for i in range(step+1,size):
      if array [i]<array[min-idx]:
        min-idx= i
        (array[step],array [min-index]=(array[min-idx],array[step])
         return array
       
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
