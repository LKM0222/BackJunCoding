#1874 스택 수열
import sys

def push(arr,n):
    arr.append(n)

def pop(arr):
    if len(arr) > 0:
        return arr.pop(len(arr) - 1)
    
    else:
        return -1

def top(arr):
    if len(arr) > 0:
        return arr[len(arr) - 1]
    else:
        return -1

def empty(arr):
    if len(arr)>0:
        return False
    else:
        return True



answer = []
stack = []
temp = []

n = int(sys.stdin.readline())

count = 0

for i in range(n):
    answer.append(sys.stdin.readline())

