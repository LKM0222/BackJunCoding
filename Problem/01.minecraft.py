import math
import statistics
import sys

#입력을 받는다.
n,m,b = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s = 0

#모든 값의 평균을 구해라?
for i in arr:
    for j in i:
        s += j

avg = round(s / (len(arr) * len(arr[0])))
print(avg)
s = 0

##필요한 블럭 갯수 구하기
for i in arr:
    for j in i:
        s += (avg - j)

print(s)
# if s > 0: #필요한 갯수가 양수면 블록을 놓아야 됨.
#     if s < b: #인벤토리에 갖고 있는 블록 수가 놔야 되는 블록 수보다 많으면 그냥 놓으면 됨
#         # 블록 놓는 구현(1초)
#     else: #블록이 없으면 블록을 깎아야됨
#         #블록 깎는 구현(2초)
