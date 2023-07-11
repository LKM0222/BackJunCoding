#1764 듣보잡
import sys
n,m = map(int,input().split())

i = set(sys.stdin.readline().rstrip() for i in range(n))
j = set(sys.stdin.readline().rstrip() for i in range(m))

x = sorted(set(i&j))
print(len(x))
for i in x:
    print(i)
            
