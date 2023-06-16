#1065 한 수

def han(n) -> int:
    s = str(n)
    if n == 999:
        return 1

    if n < 100: # 한자리와 두자리는 항상 등차수열이다.
        return 1
    
    elif n < 999: #세자리부터는 검사 필요
        d0 = int(s[1]) - int(s[0])
        d1 = int(s[2]) - int(s[1])

        if d0 == d1:
            return 1
        else:
            return 0
    
    else:
        return 0

count = 0

n = int(input())

for i in range(1,n + 1):
    #print(i, han(i),count)
    if han(i) == 1:
        count += 1
    else:
        continue

print(count)