#1041 주사위
n = int(input())
dice = list(map(int, input().split()))

temp =[]
temp.append(min(dice[0], dice[5]))
temp.append(min(dice[1], dice[4]))
temp.append(min(dice[2], dice[3]))
temp.sort()
print(temp)

one = temp[0]
two = temp[0] + temp[1]
three = sum(temp)

if n == 1:
    dice.sort()
    print(sum(dice) - dice[5])

elif n == 2:
    print(three * 4 + two * 4)

else:
    side3 = three * 4
    side2 = ((n-1) * 4 + (n-2) * 4) * two
    side1 = (((n-2) * (n-1) * 4) + ((n-2) * (n-2))) * one
    print(side3 + side2 + side1)