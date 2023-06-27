#5622 다이얼
li = "ABC DEF GHI JKL MNO PQRS TUV WXYZ".split()

s = input()

answer = 0

for i in s:
    count = 2
    for j in li:
        if i in j:
            answer += count
            count += 1
        else:
            count += 1

print(answer + len(s))
