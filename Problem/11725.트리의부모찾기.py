#11725 트리의 부모 찾기
from collections import deque
n,m,r = map(int,input().split())

visited = [False for i in range(n + 1)]
num = [0 for i in range(n)]
li = []

for i in range(m):
    li.append(list(map(int,input().split())))

  

def BFS(li,start,visited):
    count = 0
    
    visited[start] = True
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        count += 1
        num[v - 1] = count
        for i in li[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
BFS(li,r,visited)
print()
for i in num:
    print(i)
                
