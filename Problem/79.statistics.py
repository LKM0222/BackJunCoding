#2108 통계학
import sys
from collections import Counter
n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

print("\n")
arr.sort()
print(round(sum(arr) / n))
print(arr[int(len(arr) / 2)])

m = Counter(arr)
s = list(m.items())
t = []
u = []
for i in range(len(s)):
    t.append(s[i][1])
    u.append(s[i][0])



print(s, max(s),s[0][1],t,u)

print(max(arr) - min(arr))