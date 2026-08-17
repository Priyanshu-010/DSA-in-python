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

# Explanation: The selection_sort function iterates through the input list and selects the minimum element from the unsorted portion of the list. It then swaps this minimum element with the first unsorted element, effectively growing the sorted portion of the list. This process is repeated until the entire list is sorted.

# In simple words, the selection sort algorithm divides the list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest element from the unsorted part and moves it to the end of the sorted part, resulting in a fully sorted list.