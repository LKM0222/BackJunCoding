#11866

n,k= map(int,input().split())
n = list(range(1,n+1))
i = 0

newList = []

for _ in range(len(n)):
    i = i + k - 1
    if i >= len(n):
        i = i % len(n)
    newList.append(n.pop(i))
    

print("<",end='')
for i in range(len(newList)-1):
    print("%d, "%newList[i], end='')
print(newList[-1], end='')
print(">")