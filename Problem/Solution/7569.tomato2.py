#7569 토마토
#정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
import sys
from collections import deque

m, n, h = map(int,input().split())#가로 세로
arr = []

one = deque()

answer = 0

az, ay, ax = [-1,1,0,0,0,0],[0,0,-1,1,0,0], [0,0,0,0,1,-1]
for i in range(h):
    arr2 = []
    for j in range(n):
        arr2.append(list(map(int,sys.stdin.readline().split())))
    arr.append(arr2)

print(arr)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                one.append([i,j,k])



def bfs():
    while len(one) != 0:
        print(one)
        o = one.popleft()
        a,b,c = o[0],o[1],o[2]

        
        for i in arr:
            for j in i:
                print(j)

        for i in range(6):
            bx = ax[i] + c
            by = ay[i] + b
            bz = az[i] + a
            if 0 <= bx < m and 0<= by < n and 0<=bz<h and arr[bz][by][bx] == 0:
                one.append([bz,by,bx])
                arr[bz][by][bx] = arr[a][b][c] + 1

        print("")


bfs()


for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            else:
                if answer < k:
                    answer = k
    

print(answer - 1)