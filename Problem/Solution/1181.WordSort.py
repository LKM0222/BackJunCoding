#1181 단어정렬
n = int(input())

w = []
lenMax = []

for i in range(0,n):
    _str = input()
    w.append(_str)
    lenMax.append(len(_str))

value = set(w)
w = list(value)
w.sort()#일단 먼저 오름차순 정렬

for i in range(1,max(lenMax)+1):#길이
    for j in w: #길이에 맞는 문자열 탐색
        if (i == len(j)):
            print(j)