def maximum_subarray(arr):
    n = len(arr)
    
    if n > 1:
        max_sum = arr[0]
        currnet_sum = arr[0]
    
        for i in range(1, n):
            currnet_sum = max(arr[i], currnet_sum + arr[i])
            max_sum = max(max_sum, currnet_sum)

    return max_sum

arr = [-1, 3, 2, -5, 8, 9, 7]
print(maximum_subarray(arr))
