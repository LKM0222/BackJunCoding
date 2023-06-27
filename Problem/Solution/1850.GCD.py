#1850 최대공약수
def GCD(a,b):
    while b != 0:
        [a,b] = [b, a % b]
    return a

a,b = map(int,input().split())

n = GCD(a,b)

for i in range(n):
    print("1",end = "")