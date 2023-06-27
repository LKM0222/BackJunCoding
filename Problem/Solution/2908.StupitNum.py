#2908 상수
a,b = input().split()

a = a[::-1]
b = b[::-1]
if int(a) < int(b):
    print(b)
else:
    print(a)