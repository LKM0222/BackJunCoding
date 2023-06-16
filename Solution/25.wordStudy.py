#1157 단어 공부

from string import ascii_lowercase

s = input().lower()
li = list(0 for i in range(26))

for i in s:
    li[ascii_lowercase.find(i)] += 1

#가장 많이 사용 된 알파벳이 여러개인지 탐색을 해야됨...
maxx = max(li)
if li.count(max(li)) == 1:#가장 큰 수 찾을 수 있음
    print(ascii_lowercase[li.index(max(li))].upper())
else: #가장 큰 수가 여러개임
    print("?")
