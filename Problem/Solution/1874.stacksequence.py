# 1874 스택수열
import sys

n = int(sys.stdin.readline().rstrip())
arr = []
stack = []
temp = []
answer = []
numList = list(range(1,n+1))
idx = 0

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

def pop():
    # print('-')
    answer.append('-')
    temp.append(stack.pop())

def push(a):
    # print('+')
    answer.append('+')
    stack.append(a)

while idx < n:# len(stack) != 0:
    try:
        if len(stack) > 0 and arr[idx] == stack[len(stack) - 1]:
            pop()
            idx += 1
        else:
            push(numList.pop(0))
    except IndexError:
        break

    # print(stack,numList)

if arr == temp:
    for i in answer:
        print(i)

else:
    print("NO")
