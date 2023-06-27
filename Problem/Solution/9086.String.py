#9086 문자열
import sys

n = int(input())
arr = []

for _ in range(n):
    s = input()
    arr.append(s[0] + s[-1])


for i in arr:
    print(i)
