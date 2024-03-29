#14923 미로탈출
from collections import deque
import sys
import copy

n, m = map(int,sys.stdin.readline().split())
hx,hy = map(int,sys.stdin.readline().split())
ex,ey = map(int,sys.stdin.readline().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

li = []
li_copy = []

for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
    
li_copy = copy.deepcopy(li)

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if li[nx][ny] == 1:
                continue
            
            if li[nx][ny] == 0:
                li[nx][ny] = li[x][y] + 1
                queue.append((nx,ny))
    
    if li[ex - 1][ey - 1] == 1:
        return -1
    
    return li[ex - 1][ey - 1]

result = 9999999 #inf

#벽을 안부순 경우
nresult = BFS(hx -1, hy - 1)

#최솟값 구해야되니깐 비교
if result > nresult and nresult > 0:
    result = nresult
    
#벽을 부술 경우
for i in range(n):
    for j in range(m):
        if li[i][j] == 1: #벽이 있다면
            li[i][j] = 0 #빈칸으로 만들고
            nresult = BFS(hx - 1, hy - 1) #탐색을 한다.
        
        #최솟값 구해야되니깐 비교
        if result > nresult and nresult > 0:
            result = nresult
        
        # #테스트 출력 부분
        # print("case x,y : ",i + 1,j + 1)
        # print("result : ",result)
        # print("nresult : ",nresult)
        # for k in li:
        #     print(k)
        # print()
            
        #상황이 끝났다면 원래대로 만들어 두고 다시 진행
        li = copy.deepcopy(li_copy)

if result == 9999999:
    print(-1)
else:
    print(result)