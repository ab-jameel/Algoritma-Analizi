def bubble_sort(arr):
    l = len(arr)
    if l > 1:
        for i in range(l):
            swapped = False
            for j in range(l - i - 1):
                if arr[j+1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

            if not swapped:
                break

    return arr

arr = [-1, 3, 2, -5, 8, 9, 7]
print(bubble_sort(arr))