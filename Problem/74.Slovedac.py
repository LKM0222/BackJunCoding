#18110 Solved.ac

n = int(input())
s = []
r = round(n * 0.15)
x = 0
for i in range(n):
    s.append(int(input()))

s.sort()
for i in range(r,n-r):
    x += s[i]

y = (n - r * 2)

if y > 0:
    print(round(x / y))
else:
    print(0)
