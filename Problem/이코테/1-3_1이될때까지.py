#n = 어떤 수, k 나눌수
n, k = map(int, input().split())

count = 0
while n != 1:
    if(n % k == 0): #나누어 떨어진다면
        n = n // k
    
    else:
        n -= 1
    
    count += 1

print(count)