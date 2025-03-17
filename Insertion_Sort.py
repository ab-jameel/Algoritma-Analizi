def insertion_sort(arr):
    n = len(arr)
    if n > 1:
        for i in range(1, n):
            j = i - 1
            key = arr[i]

            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    
    return arr

arr = [-1, 3, 2, -5, 8, 9, 7]
print(insertion_sort(arr))
