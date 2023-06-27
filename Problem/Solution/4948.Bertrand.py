#4948 베르트랑 공준

import sys
input = sys.stdin.readline

def Prime(n):
    if n == 1: return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0: return False

    return True

li = list(range(2,123456 * 2 + 1))
arr = []

for i in li:
    if Prime(i): arr.append(i)

while True:
    n = int(input())
    count = 0
    if n == 0: break   
    for i in arr:
        if n < i <= n * 2:
            count+= 1
        

    print(count)
    