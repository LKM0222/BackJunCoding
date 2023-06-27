#1978 소수찾기
#일단 소수를 판정하는 프로그램만 짜면 해결
def Prime(n) -> bool:
    if n == 1:
        return False
    
    if n == 2:
        return True

    for i in range(2,n):
        if n % i == 0:  
            return False
        
    return True

t = int(input())
li = list(map(int,input().split(' ')))
count = 0
for n in li:
    if Prime(n): count += 1

print(count)