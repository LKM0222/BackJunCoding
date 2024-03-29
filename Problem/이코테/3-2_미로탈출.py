import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

li = []

for i in range(n):
    li.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while(queue):
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
                
    return li[n-1][m-1]

print(bfs(0,0))