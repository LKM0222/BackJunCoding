#2751
import sys

n = int(input())

numlist = []

for i in range(0,n):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()

for i in numlist:
    print(i)