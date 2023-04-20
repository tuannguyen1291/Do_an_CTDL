def insertion_sort(arr):
    # Vòng lặp bắt đầu từ phần tử thứ hai của mảng
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Di chuyển các phần tử có giá trị lớn hơn giá trị khóa đến một vị trí trước
        # vị trí hiện tại của nó trong mảng sắp xếp.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Chèn giá trị khóa vào vị trí đúng trong mảng sắp xếp
        arr[j + 1] = key
    return arr

# ví dụ sử dụng
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Mảng đã sắp xếp: ", sorted_arr)
