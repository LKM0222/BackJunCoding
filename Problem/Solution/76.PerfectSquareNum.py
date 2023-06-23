#1977 완전제곱수 (완)
m = int(input())
n = int(input())
s= 0
num = []


for i in range(m,n+1):
    if float(i ** (1/2)).is_integer():
        num.append(i)

for i in num:
    s += i

if len(num) > 0:
    print(s)
    print(num[0])
else:
    print(-1)
