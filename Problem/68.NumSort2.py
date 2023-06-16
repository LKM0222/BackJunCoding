#2751
n = int(input())

numlist = []

for i in range(0,n):
    a = int(input())
    numlist.append(a)

numlist.sort()

for i in numlist:
    print(i)