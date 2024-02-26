n = int(input())

dx = [-1, 1, 0, 0] #LRUD
dy = [0, 0, -1, 1] #LRUD

x,y = 1,1

li = list(input().split())

for i in li:
    if i == 'L':
        if not(x - 1 == 0):
            x += dx[0]
            y += dy[0]
    if i == 'R':
        if not(x + 1 == n):
            x += dx[1]
            y += dy[1]
    if i == 'U':
        if not(y - 1 == 0):
            x += dx[2]
            y += dy[2]
    if i == 'D':
        if not(y + 1 == n):
            x += dx[3]
            y += dy[3]

print(y, x)
#문제에서는 x,y의 좌표가 대칭 이동 되어있기 때문에 y,x로 출력한다.