#10773 제로
from collections import deque

n = int(input())
li = deque()

for _ in range(n):
    x = int(input())
    if x != 0:
        li.append(x)
    else:
        li.pop()

print(sum(li))