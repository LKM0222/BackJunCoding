#18110 Solved.ac
import sys

def roundNum(n):
    return int(n) + [0, 1][n - int(n) >= 0.5]

n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)
else:
    arr = []
    for i in range(n):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort()
    r = roundNum(n * 0.15)
    if r > 0: arr = arr[r:-r]
    print(roundNum(sum(arr) / len(arr)))