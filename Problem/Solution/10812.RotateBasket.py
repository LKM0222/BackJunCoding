#10812 바구니 순서 바꾸기
n, m = map(int,input().split())

li = list(range(1,n+1))
#print(li)

for i in range(m):
    tmp = []
    begin, end, mid = map(int,input().split())
    count = mid - 1
    for i in range(end - begin + 1):
        if count + 1 > end:
            count = begin - 1

        tmp.append(li[count])
        count += 1

    #print("now tmp ", tmp,", ",begin,end,mid)
    li[begin - 1:end] = tmp
    #print("li is ",li)

for i in li:
    print(i,end=' ')
    
