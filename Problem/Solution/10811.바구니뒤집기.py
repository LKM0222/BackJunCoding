#10811.바구니뒤집기.py

n,m = map(int,input().split())

arr = list(range(1,n+1))


for i in range(m):
    x,y = map(int,input().split())
    
    temp = arr[x-1:y]
    temp.reverse()
    
    arr[x-1:y] = temp

for i in arr:
    print(i,end=' ')