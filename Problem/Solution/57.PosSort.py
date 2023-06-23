#11650 좌표 정렬하기

n = int(input())
arr = []

for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()

for i in arr:
    print(i[0],i[1])