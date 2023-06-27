#10810 공 넣기

n, m = map(int,input().split())

li = [0  for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    
    for x in range(a - 1,b):
        li[x] = c

for i in li:
    print(i, end=' ')