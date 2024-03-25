#2805 나무자르기
import sys

n, m = map(int,input().split())

li = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(li)

result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for i in li:
        if i > mid:
            total += i - mid
            
    if total < m: #총 합이 찾을 값보다 크다면
        end = mid - 1
    else:
        result = mid #일단 최소값을 찾아야 하니까 result에 저장.
        start = mid + 1

print(result)
