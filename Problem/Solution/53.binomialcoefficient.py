#11050 이항계수 1

n,k = map(int,input().split())

count = 0
diff = n - k
a,b = 1,1
if diff <= k:
    for i in range(n,n-k,-1):
        count += 1
        a *= i

    for i in range(count,0,-1):
        b *= i

else:
    for i in range(n,k ,-1):
        count += 1
        a *= i

    for i in range(count,0,-1):
        b *= i

print(a//b)
