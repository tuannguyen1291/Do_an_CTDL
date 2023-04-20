def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Khởi tạo một mảng
arr = [64, 34, 25, 12, 22, 11, 90]

# Sắp xếp mảng
sorted_arr = bubbleSort(arr)

# In kết quả
print("Mảng đã sắp xếp là:")
for i in range(len(sorted_arr)):
    print("%d" %sorted_arr[i]),
