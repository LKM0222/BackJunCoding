#2178 미로탐색
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())

li = []
for i in range(n):
    li.append(list(map(int,input())))
    
    
def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if li[nx][ny] == 0:
                continue
            
            if li[nx][ny] == 1:
                li[nx][ny] = li[x][y] + 1
                queue.append((nx,ny))
    
    return li[n - 1][m - 1]

print(BFS(0,0))