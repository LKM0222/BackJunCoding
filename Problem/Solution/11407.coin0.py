#11407 동전 0
n, value = map(int, input().split())
coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

for i in range(len(coin)-1, -1, -1):
    if coin[i] <= value:
        count += value // coin[i]
        value = value % coin[i]
        
print(count)