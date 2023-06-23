#1546 평균

n = int(input())
li = list(map(int,input().split()))
maxx = max(li)
temp = []
for i in li:
    temp.append(i / maxx * 100)

print(sum(temp) / n)