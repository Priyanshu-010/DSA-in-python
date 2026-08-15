arr = [14,2,5,1,3,7,9,8,6,4]

def selection_sort(arr):
  n = len(arr)
  for i in range(0, n):
    min_index = i
    for j in range(i+1, n):
      if arr[min_index] > arr[j]:
        min_index = j

    if min_index != i:  #Just for optimization not required for sorting
      arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(arr)
print(arr)