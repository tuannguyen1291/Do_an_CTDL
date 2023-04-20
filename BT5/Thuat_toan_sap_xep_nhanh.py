def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

# ví dụ sử dụng
arr = [5, 2, 8, 4, 7, 6, 1, 3]
print("Before sorting: ", arr)
arr = quicksort(arr)
print("After sorting: ", arr)
