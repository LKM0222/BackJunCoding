#10813 공 바꾸기 구현
n,m = map(int,input().split())

arr = list(range(1,n+1))

for i in range(m):
    x,y = map(int,input().split())
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
    
for i in arr:
    print(i,end=" ")