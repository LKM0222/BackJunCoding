#안전영역 (그래프이론, 브루트포스알고리즘, 깊이우선탐색)
import sys
import copy
n = int(input())
sys.setrecursionlimit(100000)

arr = []
arr_Copy = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# m = max(max(arr)) #최댓값 구할때 이렇게 구하면 안됨.
max = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > max:
            max = arr[i][j]

arr_Copy = copy.deepcopy(arr)

def dfs(x,y,lim):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if arr[x][y] > lim:
        arr[x][y] = lim #방문처리

        dfs(x+1, y, lim)
        dfs(x, y+1, lim)
        dfs(x-1, y, lim)
        dfs(x, y-1, lim)
        return True
    return False

result = 0
answer = 0
for i in range(0, max):
    for j in range(n):
        for k in range(n):
            if dfs(j,k,i):
                answer += 1
    
    if result < answer:
        result = answer
    
    arr = copy.deepcopy(arr_Copy)
    answer = 0

print(result)