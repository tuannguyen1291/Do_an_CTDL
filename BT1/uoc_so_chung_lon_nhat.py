def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
print(gcd(a,b))
