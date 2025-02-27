def selectionSort(array, size):
   
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
         # swap
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [2, 3, 5, 7, 9,11,12,4]
size = len(arr)
selectionSort(arr, size)
print('EX:2 - The array after sorting by selection sort is: ', arr)
