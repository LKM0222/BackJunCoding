#2675 문자열 반복

n = int(input())
for i in range(n):
    li = list(input().split())
    repeat = int(li[0])
    temp = ""
    for j in li[1]:
        for _ in range(repeat):
            temp += j
    
    print(temp)
