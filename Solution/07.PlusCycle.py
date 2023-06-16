#1110
n = input() #얜 일단 무조건 str이다.
temp = n
cycle = 0

while True:
    cycle += 1
    
    if int(n) == 0:
        break

    #print("cy",cycle)

    if int(n) < 10:
        n = n+n
    else:
        if int(n[0]) + int(n[1]) < 10:
            if int(n[1]) == 0:
                n = str(int(n[0]) + int(n[1]))
            else:
                n = n[1] + str(int(n[0]) + int(n[1]))
        else:
            tp = str(int(n[0]) + int(n[1]))
            n = n[1] + tp[1]
    #print(n, temp)
    if temp == n:
        break

print(cycle)