#7568 덩치
n = int(input())
li = []
answer = []
for _ in range(n):
    x,y = map(int,input().split())
    li.append([x,y])

for i in li:
    count = 1
    for j in li:
        if i[0] < j[0]:
            if i[1] < j [1]:
                count += 1

    answer.append(count)

for i in answer:
    print(i,end=' ')
