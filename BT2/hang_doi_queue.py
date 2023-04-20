import queue

# Tạo một hàng đợi rỗng với kích thước tối đa là 5
q = queue.Queue(maxsize=5)

# Thêm các phần tử vào hàng đợi
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

# Hiển thị số lượng phần tử trong hàng đợi
print("Số phần tử trong hàng đợi là:", q.qsize())

# Lấy các phần tử ra khỏi hàng đợi và in ra màn hình
while not q.empty():
    print(q.get())

# Hiển thị số lượng phần tử trong hàng đợi sau khi đã lấy ra tất cả các phần tử
print("Số phần tử trong hàng đợi sau khi lấy ra là:", q.qsize())
