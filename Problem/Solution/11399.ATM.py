#11399 ATM

n = int(input())
li = list(map(int, input().split()))

li.sort()
s = 0
for i in range(1, len(li) + 1):
    s += sum(li[0:i])

print(s)