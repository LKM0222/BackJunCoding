#2108 통계학
import sys
from collections import Counter
n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

# print("\n")
arr.sort()
print(round(sum(arr) / n))
print(arr[int(len(arr) / 2)])

#최빈값 중 두번째로 작은 값 구하는 코드 짜야됨.
m = Counter(arr) #각 항목마다 갯수 구하기
m = list(m.items())
maxnum = max(m,key=lambda x:x[1])[1]
maxnumli = []
for i in m:
    if i[1] == maxnum:
        maxnumli.append(i)


if len(maxnumli) > 1:
    maxnumli.sort(key=lambda x: x[0])
    print(maxnumli[1][0])
else:
    print(maxnumli[0][0])



print(max(arr) - min(arr))