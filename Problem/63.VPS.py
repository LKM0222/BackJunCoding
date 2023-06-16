#9012 괄호
n = int(input())

for i in range(n):
    count = 0
    s = input()
    tmp = []

    for i in s:
        if i == "(":
            count += 1
            tmp.append(i)