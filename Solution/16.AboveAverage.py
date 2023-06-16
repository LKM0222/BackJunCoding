#4344 평균은 넘겠지...!
"""
for i in range(int(input())):
    li = list(map(int,input().split()))
    n = li[0]
    li = li[1:]
    avr = sum(li) / n
    count = 0
    for j in li:
        if j > avr:
            count += 1
    print("{:.3f}".format((count / n) * 100),"%")
"""
num = int(input())

for _ in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')