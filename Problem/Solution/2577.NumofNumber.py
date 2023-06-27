#2577 숫자의 갯수
a = int(input())
b = int(input())
c = int(input())
n = str(a * b * c)

count = [0 for _ in range(10)]

for i in n:
    count[int(i)] += 1

for i in count:
    print(i)