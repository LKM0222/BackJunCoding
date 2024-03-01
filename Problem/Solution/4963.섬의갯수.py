#4963 섬의 갯수(그래프이론, 그래프탐색, 너비우선탐색, 깊이우선탐색)
#1은 땅, 0은 바다
#첫째줄에 지도의 크기 가로세로 w h
#두번째줄부터 지도 입력
#지도의 크기가 0 0 이면 입력 종료
import sys
sys.setrecursionlimit(10**9)
li = []

def dfs(x,y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    
    if li[x][y] == 1:
        li[x][y] = 0 #방문처리
        
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y+1) #대각선이 이어져있어도 동일함.
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y-1)
        
        return True
    return False

while True:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    for i in range(h):
        li.append(list(map(int,sys.stdin.readline().split())))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    
    
    print(result)
    li.clear()