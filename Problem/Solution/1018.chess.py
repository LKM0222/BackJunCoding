#1018 체스판 다시 칠하기
import sys

n,m = map(int, input().split())

arr = []

spare = []

min = 99
e = ''#짝
o = ''#홀
count = 0
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())


def GetChess(a,b):
    if a <= n - 8 and b <= m - 8:
        for i in range(a,a+8):
            temp = []
            for j in range(b,b + 8):
                temp.append(arr[i][j])
            
            spare.append(temp)

def CheckChess(e,o):
    c = 0
    for a in range(8):
            for b in range(8):
                    if (a + b) % 2 == 0:
                        if spare[a][b] == e:
                            continue
                        else:
                            c+= 1

                    else:
                        if spare[a][b] == o:
                            continue
                        else:
                            c += 1

    return c


for i in range(n-7):
    for j in range(m - 7):
        spare.clear()
        GetChess(i,j)

        count = CheckChess('B','W')
        if min > count:
            min = count
        
        count = CheckChess('W','B')
        if min > count:
            min = count

        # count = 0


print(min)


