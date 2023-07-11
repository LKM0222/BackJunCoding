#1003 피보나치 함수
n = int(input())
for _ in range(n):
    a,b = 1,0
    x = int(input())
    for i in range(x):
        a,b = b,a+b
    print(a,b)