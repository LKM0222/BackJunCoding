#2581 소수
#M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램

def Prime(n) -> bool:
    if n == 1: return False
    if n == 2: return True

    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True


m = int(input())
n = int(input())
s = 0
count = 0
li = []

for i in range(m,n+1,1):
    if Prime(i): 
        li.append(i)
        count += 1

if count > 0:
    print(sum(li))
    print(min(li))
    
else: print(-1)