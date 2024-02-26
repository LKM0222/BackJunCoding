#n = 행, m = 열
n, m = map(int, input().split())

maxi = 0

for i in range(0,n):
    li = list(map(int, input().split()))
    li.sort()
    if(li[0] > maxi):
        maxi = li[0]

print(maxi)