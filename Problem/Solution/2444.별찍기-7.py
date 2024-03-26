#2444 별찍기 7
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input())

for i in range(n): #위쪽
    for j in range(n-1-i): #띄어쓰기
        print(" ",end='')
    
    for k in range((i+1)*2-1):#별찍기
        print("*",end='')
    print()
    
for i in range(n-1): #아래쪽
    for j in range(i+1): #띄어쓰기
        print(" ",end='')
    
    for k in range((n-1-i)*2-1):
        print("*",end='')
    
    print()
    