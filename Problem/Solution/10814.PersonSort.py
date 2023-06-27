#10814
# n = int(input())

# person = []
# people = []
# maxAge = 0
# minAge = 9999999

# for i in range(0,n):
#     age, name = input().split()
#     person.append({age:name})

# for i in person:
#     a = str(i.keys())
#     intA = int(a[12:-3])
#     if intA > maxAge:
#         maxAge = intA 
#     if intA < minAge:
#         minAge = intA


# for i in range(minAge,maxAge + 1):
#     for j in person:
#         jk = str(j.keys())
#         jv = str(j.values())
#         jKey = int(jk[12:-3])
#         jValues = jv[14:-3]
#         if jKey == i:
#             print(str(jKey) +" "+str(jValues))
import sys
input = sys.stdin.readline

n = int(input())
user = []

for _ in range(n):
    user.append(list(input().split()))

user.sort(key= lambda a:int(a[0]))

for i in range(n):
    print(user[i][0], user[i][1])