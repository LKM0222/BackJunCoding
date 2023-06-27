#1259 펠린드롬수
n = input()
while n != "0":
    flag = True
    #print(n[0],n[1],n[2],n[-1],n[-2],n[-3])
    for i in range(len(n) // 2):
        if n[i] != n[-i-1]:
            flag = False
            break

    if flag: print("yes")
    else : print("no")

    n = input()