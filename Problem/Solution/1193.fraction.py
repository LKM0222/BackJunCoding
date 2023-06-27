#1193 분수찾기

def sn(n) -> int:
    return 1 + ((n +  n * n) // 2)

i = int(input())
n = 0

while True:
    s = sn(n)
    if i < s:
        if n % 2 == 0:
            #print(n, sn(n) - 1 , sn(n - 1))
            x = sn(n) - 1 - i#분자
            y = i - sn(n - 1)#분모
            #print(x,y)
            print(str(n - x)+"/"+str(n - y))
            break
        else:
            #print(n, sn(n) - 1 , sn(n - 1))
            x = sn(n - 1)- i#분자
            y = sn(n) - 1 - i #분모
            #print(x,y)
            print(str(n + x)+"/"+str(n - y))
            break
        
    n += 1