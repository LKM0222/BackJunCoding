#25206 너의 평점은
import sys

avg = 0
count = 0

for i in range(20):
    name,n,score = sys.stdin.readline().split()
    
    n = float(n)
    
    if score == 'A+':
        avg += n * 4.5
        count += n
    elif score == 'A0':
        avg += n * 4.0
        count += n
    elif score == 'B+':
        avg += n * 3.5
        count += n
    elif score == 'B0':
        avg += n * 3.0
        count += n
    elif score == 'C+':
        avg += n * 2.5
        count += n
    elif score == 'C0':
        avg += n * 2.0
        count += n
    elif score == 'D+':
        avg += n * 1.5
        count += n
    elif score == 'D0':
        avg += n * 1.0
        count += n
    elif score == 'F':
        count += n
    else:
        continue

# print('avg is ', avg, ', count is ', count)
print(avg/count)
        