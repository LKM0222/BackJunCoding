#2920 음계
n = list(map(int,input().split(" ")))


if n[0] == 1:
    count = 1
    for i in n:
        if count == i:
            if count == 8 and count == i:
                print("ascending")
                break
            count += 1
            continue
        else:
            print("mixed")
            break


elif n[0] == 8:
    count = 8
    for i in n:
        if count == i:
            if count == 1 and count == i:
                print("descending")
                break
            count -= 1
            continue
        else:
            print("mixed")
            break
else:
    print("mixed")

