#11651 좌표정렬하기 2
from collections import deque
n = int(input())
li = []

for _ in range(n):
    x,y = map(int,input().split())
    li.append([x,y])
li.sort(key = lambda x:x[0])
li.sort(key= lambda x:x[1])

for i in li:
    print(i[0], i[1])