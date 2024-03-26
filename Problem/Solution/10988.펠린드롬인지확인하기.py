# 10988 펠린드롬인지 확인하기 구현

s = input()

mid = len(s) //2

if len(s) % 2 == 1: #길이가 홀수라면
    mid += 1 #mid에 1 더해주기
    
if len(s) % 2 == 0: #길이가 짝수라면
    front = list(s[0:mid])
    end = list(s[mid:len(s)])
    end.reverse()
    if front == end:
        print("1")
    else:
        print("0")

else: #길이가 홀수라면
    front = list(s[0:mid-1])
    end = list(s[mid:len(s)])
    end.reverse()
    if front == end:
        print("1")
    else:
        print("0")