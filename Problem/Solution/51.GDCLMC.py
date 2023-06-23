#2609  최대공약수 최소공배수 
a,b = map(int,input().split())
c,d = a,b
gdc = 0
lmc = 0

while c != d:
    if c > d:
        c -= d
    else:
        d -= c
    
print(c)

print(a * b // c)