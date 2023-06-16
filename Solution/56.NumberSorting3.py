#10989 수 정렬하기 3
"""
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x = int(sys.stdin.readline())
    arr.append(x)

arr.sort()
for i in arr:
    print(i)"""

import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    check_list[input_num] = check_list[input_num] + 1
    
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)