#7576 토마토
#정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
import sys
from collections import deque

m, n = map(int,input().split())#가로 세로
arr = []
one = deque()

answer = 0

ay, ax = [-1,1,0,0], [0,0,1,-1]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            one.append([i,j])

def bfs():
    while len(one) != 0:
        o = one.popleft()
        x ,y = o[1],o[0]

        for i in range(4):
            by, bx = ay[i] + y , ax[i] + x
            if 0 <= by < n and 0 <= bx < m and arr[by][bx] == 0:
                one.append([by,bx])
                arr[by][bx] = arr[y][x] + 1

bfs()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(i))

print(answer - 1)
    
