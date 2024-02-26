n, m, k = map(int, input().split())

li = list(map(int, input().split()))

li.sort()

one = li[n - 1]
two = li[n - 2]

count = 0
result = 0
for i in range(0,m):
    if count == k:
        result += two
        count = 0
    else:
        result += one
        count += 1
      
print(result)