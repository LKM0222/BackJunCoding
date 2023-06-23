#1929 소수구하기
import math
import sys
input = sys.stdin.readline
def Prime(n):
    if n == 1: return False
    sq = int(math.sqrt(n))

    for i in range(2,sq+1):
        if n % i == 0: return False

    return True


n,m = map(int,input().split())
for i in range(n,m+1):
    if Prime(i): print(i)