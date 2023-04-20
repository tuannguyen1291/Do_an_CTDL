def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Nhập vào số cần tính giai thừa: "))
a=factorial(n)
print(a)