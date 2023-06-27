#1018 체스판 다시 칠하기
import sys

n,m = map(int, input().split())

arr = []

for i in range(n):
    arr.append([list(sys.stdin.readline().rstrip())])

for i in arr:
    print(i)