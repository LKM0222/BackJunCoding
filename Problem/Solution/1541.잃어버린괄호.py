#1541 잃어버린 괄호 (그리디, 수학, 문자열, 파싱)
import sys
s = sys.stdin.readline()

num = []
n = ''

minusFlag = False

for i in s:
    if not(i == '+' or i == '-'): #기호가 아니라면
        n += i #숫자를 문자열로 일단 저장
    else: #기호라면
        num.append(int(n))
        n = ''
        num.append(i)

num.append(int(n)) #마지막 저장된 수도 추가.

answer = num[0]
temp = 0
for i in range(1,len(num)):
    if not(num[i] == '+' or num[i] == '-'):
        if minusFlag:
            temp += num[i]
        else:
            answer += num[i]
        # print("answer:",answer,"temp:",temp)

    else:
        if num[i] == '-':
            minusFlag = True
            answer -= temp
            temp = 0
    
if minusFlag:
    answer -= temp
else:
    answer += temp
print(answer)