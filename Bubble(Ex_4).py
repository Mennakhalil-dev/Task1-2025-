def bubble_sort(arr,size):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [10,7,3,9,2]
size = len(arr)
bubble_sort(arr, size)
print('EX:4 - The array after sorting by Bubble sort is: ', arr)

