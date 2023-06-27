#2231 분해합

n = int(input())
arr = []

for i in range(1,n + 1):
    li = list(str(i))
    s = i
    for j in li:
        s += int(j)
        

    if s == n:
        arr.append(i)

    if i == n:
        minn = 0

if len(arr) == 0:
    print(0)
else: print(min(arr))
