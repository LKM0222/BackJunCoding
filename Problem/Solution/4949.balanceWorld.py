#4949 균형잡힌 세상
import sys
from collections import deque

s = sys.stdin.readline().rstrip()


while s != '.':
    noFlag = True
    stack = deque()
    try:
        for i in s:
            if i == '.':
                break
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']' or i == ')':
                x = stack[len(stack) - 1]
                if (i == ']' and x == '[') or (i == ')' and x == '('):#마지막에 들어온 괄호의 유형과 현재 비교하는 괄호의 유형이 같다면
                    stack.pop()
                    continue
                else:
                    noFlag = False
                    break
    except IndexError:
        noFlag = False

    if len(stack) == 0 and noFlag:
            print("yes")
    else:
        print('no')
    
    s = sys.stdin.readline().rstrip()