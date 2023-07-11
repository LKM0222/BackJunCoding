#11723 집합
import sys
s = set()

def ad(n):
    global s
    s.add(n)

def re(n):
    global s
    if n in s:
        s.remove(n)
    else:
        pass

def ch(n):
    global s
    if n in s:
        print(1)
    else:
        print(0)

def to(n):
    global s
    if n in s:
        s.remove(n)
    else:
        s.add(n)

def al():
    global s
    s = set(i for i in range(1,21))

def em():
    global s
    s.clear()

n = int(sys.stdin.readline().rstrip())


for i in range(n):
    operator = list(sys.stdin.readline().rstrip().split())
    if operator[0] == 'add':
        ad(int(operator[1]))
    elif operator[0] == 'remove':
        re(int(operator[1]))
    elif operator[0] == 'check':
        ch(int(operator[1]))
    elif operator[0] == 'toggle':
        to(int(operator[1]))
    elif operator[0] == 'all':
        al()
    elif operator[0] == 'empty':
        em()
    
    print(s)