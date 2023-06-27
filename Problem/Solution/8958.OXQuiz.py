#8958 OX퀴즈

li = []
for i in range(int(input())):
    li.append(input())

score = []
for i in li:
    n = 0
    sum = 0
    count = 1
    while n < len(i):
        if i[n] == 'O':
            sum += count
            count += 1
        
        else:
            count = 1
        
        n += 1

    n = 0
    score.append(sum)
    sum = 0

for i in score:
    print(i)