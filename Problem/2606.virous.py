#2606 바이러스
from collections import deque
n = int(input())
m = int(input())
v = [0]
visitFalg = [False for i in range(n + 1)]
print(visitFalg)

for i in range(m):
    x,y = map(int,input().split())
    v.append([x,y])

def bfs(start):
    # visit = []
    queue = deque([start])
    visitFalg[start] = True

    while queue:
        z = queue.popleft()
        print(z, end=' ')
        for i in v[z]:
            print(v[z], "i is ",i)
            if not visitFalg[i]:
                visitFalg[i] = True
                queue.append(i)

    
bfs(1)