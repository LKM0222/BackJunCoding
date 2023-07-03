#1966 프린터큐
from collections import deque

n = int(input())

for i in range(n):
    c , q = map(int,input().split())

    li = deque(map(int,input().split()))

    count = 0
    while q != -1:
        m = max(li)
        x = li.popleft()
        
        if q == 0:
            if x == m:
                count += 1
                print(count)
                q -= 1
            else:
                li.append(x)
                q = len(li) - 1#맨마지막

        else:
            if x == m:
                count += 1
                q -= 1
            else:
                li.append(x)
                q -= 1


    


    