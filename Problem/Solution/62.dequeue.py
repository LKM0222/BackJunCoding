#10866 덱
import sys


def push_back(n):
    arr.append(n)

def push_front(n):
    arr.insert(0,n)

def pop_front():
    if size() > 0:
        return arr.pop(0)
    else:
        return -1

def pop_back():
    if size() > 0:
        return arr.pop(size() - 1)
    else:
        return -1

    
def size():
    return len(arr)


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

def empty():
    if size() > 0:
        return 0
    else:
        return 1

n = int(input())
arr = []

for i in range(n):
    code = list(sys.stdin.readline().split())

    if code[0] == "push_front":
        push_front(code[1])
    if code[0] == "push_back":
        push_back(code[1])
    if code[0] == "pop_front":
        print(pop_front())
    if code[0] == "pop_back":
        print(pop_back())
    if code[0] == "front":
        print(front())
    if code[0] == "back":
        print(back())
    if code[0] == "empty":
        print(empty())
    if code[0] == "size":
        print(size())