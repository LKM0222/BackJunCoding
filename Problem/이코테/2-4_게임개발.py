#다시풀어보기

n,m = map(int,input().split())

x,y,d = map(int,input().split())

arr= []
for i in range(n):
    arr.append(list(map(int,input().split())))


dx = [-1,0,1,0] #서남동북(반시계방향)
dy = [0,-1,0,1]
darr = [3,2,1,0]#서남동북

count = 0

def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if()