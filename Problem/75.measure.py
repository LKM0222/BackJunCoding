#2501 약수 구하기
n, k = map(int,input().split())
m = []

for i in range(1,n+1):
    if n % i == 0:
        m.append(i)

if len(m) > k:
    print(m[k - 1])
else:
    print(0)
