def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
         # swap
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [10,7,3,9,2]
size = len(arr)
selectionSort(arr, size)
print('Ex:4 - The array after sorting by selection sort is: ', arr)
