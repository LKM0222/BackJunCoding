#10845 큐
import sys

def size():
    return len(arr)


def pop():
    if size() > 0:
        return arr.pop(0)
    else:
        return -1

def front():
    if size() > 0:
        return arr[0]
    else:
        return -1

def back():
    if size() > 0:
        return arr[size() - 1]
    else:
        return -1

def push(n):
    arr.append(n)

def empty():
    if size() > 0:
        return 0
    else:
        return 1

n = int(input())
arr = []

for i in range(n):
    code = list(sys.stdin.readline().split())

    if code[0] == "push":
        push(code[1])
    if code[0] == "pop":
        print(pop())
    if code[0] == "front":
        print(front())
    if code[0] == "back":
        print(back())
    if code[0] == "empty":
        print(empty())
    if code[0] == "size":
        print(size())