#4153 직각삼각형

a,b,c = map(int,input().split(' '))


while a != 0 and b != 0 and c != 0:
    flag = False
    if a > b and a > c:
        if (b ** 2 + c ** 2) == a ** 2:
            flag = True
        else:
            flag = False
    if b > c and b > a:
        if (a ** 2 + c ** 2) == b ** 2:
            flag = True
        else:
            flag = False
    if c > a and c >b:
        if (b ** 2 + a ** 2) == c ** 2:
            flag = True
        else:
            flag = False
    
    if flag: print("right")
    else: print("wrong")

    a,b,c = map(int,input().split(' '))