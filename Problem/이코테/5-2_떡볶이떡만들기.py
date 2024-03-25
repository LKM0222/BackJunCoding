import sys
# sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

li = list(map(int,input().split()))

start = 0
end = max(li)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
        
    for i in li:
        if i > mid:
            total += i - mid
        
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
                
# print(max(li) - Binary(li,m,0,max(li) - 1))