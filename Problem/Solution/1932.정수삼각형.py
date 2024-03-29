#1932 정수삼각형 (다이나믹 프로그래밍)
n = int(input())

arr = []

for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)


for i in range(n-2, -1, -1): #아래에서부터 자기 자식 둘을 더해서 큰쪽을 자기자신으로 만들기
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j + 1], arr[i+1][j])
    

print(arr[0][0])