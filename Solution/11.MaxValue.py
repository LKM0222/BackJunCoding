#2562
li = []
for i in range(9):
    num = int(input())
    li.append(num)

n = 0
for i in range(9):
    if li[i] == max(li):
        n = i + 1
        break

print(max(li))
print(n)