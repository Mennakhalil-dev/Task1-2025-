def insertionSort(arr,size):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [2, 3, 5, 7, 9,11,12,4]
size = len(arr)
insertionSort(arr, size)
print('EX:2 - The array after sorting by insertion sort is: ', arr)

