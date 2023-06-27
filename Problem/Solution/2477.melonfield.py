#2477 참외밭
import math
n = int(input())

length = []
h = []
v = []

for _ in range(6):
    li = list(map(int,input().split()))
    length.append(li[1])
    if li[0] == 1 or li[0] == 2:
        h.append(li[1])
    else:
        v.append(li[1])

bigSq = max(h) * max(v)

idxH = length.index(max(h))
idxV = length.index(max(v))
#인덱스가 0일 경우 1과 5를 더해야함 나머지는 알아서~~



smallH = int(math.fabs(length[(idxH + 1) % 6] - length[idxH - 1]))
smallV = int(math.fabs(length[(idxV + 1) % 6] - length[idxV - 1]))


smallSq = smallH * smallV
print((bigSq - smallSq) * n)
