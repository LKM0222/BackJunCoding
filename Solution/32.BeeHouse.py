#2292 벌집

i = int(input())
n = 0
sn = 0

while sn < 1000000000:
    n  += 1
    sn = 1 + (n * ( 2 + (n -1) * 6)) // 2 - (n - 1)
    if i < sn:
        print(n)
        break