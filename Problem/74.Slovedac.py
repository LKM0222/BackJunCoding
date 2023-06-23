#18110 Solved.ac

def roundNum(n):
    if n > int(n) + 0.49:
        return int(n+1)
    else:
        return int(n)
    

n = int(input())
s = []
r = int(roundNum(n * 0.15))
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


