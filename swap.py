def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
arr = [1, 2, 3, 4]
swap(arr, 1, 3)
print(arr)
