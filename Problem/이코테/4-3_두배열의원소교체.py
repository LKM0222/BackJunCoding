n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(n):
    if a[i] < b[i] and k > 0:
        a[i], b[i] = b[i], a[i]
        k -= 1
        
print(sum(a))