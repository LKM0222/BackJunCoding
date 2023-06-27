#1361 그룹단어체커

def checker(s):
    li = []
    for i in range(len(s)):
        if s[i] in li:
            if s[i] != s[i-1]:
                return 0
        else:
            li.append(s[i])

    return 1


n = int(input())
count = 0
for i in range(n):
    s = input()
    if checker(s) != 0:
        count += 1
    else:
        continue
    
print(count)