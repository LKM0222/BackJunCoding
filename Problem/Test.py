import sys

for _ in range(3):
    sumis = 0
    n = int(input())
    for i in range(n):
        sumis += int(sys.stdin.readline().rstrip())
        
    if sumis == 0:
        print(0)
    elif sumis > 0:
        print('+')
    else:
        print('-')