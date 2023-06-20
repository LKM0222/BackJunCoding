#1676 팩토리얼 0의 갯수
import math
s = str(math.factorial(int(input())))[::-1]
# s = s[::-1]
i = 0
while s[i] == '0':
    i += 1

print(i)
