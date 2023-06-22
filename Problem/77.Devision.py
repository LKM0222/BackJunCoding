#1075 나누기 (완)
n = input()
f = int(input())

for i in range(100):
    if i < 10:
        s = n[0:-2] + "0" + str(i)
        if int(s) % f == 0:
            print("0"+str(i))
            break
    
    else:
        s = n[0:-2] + str(i)
        if int(s) % f == 0:
            print(str(i))
            break
        