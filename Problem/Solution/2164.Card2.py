#2164 카드2
n = int(input())

li = list(range(1,n + 1))

while len(li) > 1:
    if len(li) % 2 == 0:
        li = li[1::2]
        #print(li)
    else:
        li = [li[len(li) - 1]] + li[1::2]
        #print(li)
    


print(li[0])