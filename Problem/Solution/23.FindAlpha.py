#10809 알파벳 찾기
from string import ascii_lowercase

lowerAlpha = list(ascii_lowercase)
arr = [0 for i in range(26)]
s = input()

for i in range(len(lowerAlpha)):
    if lowerAlpha[i] in s:
        arr[i] = int(s.find(lowerAlpha[i]))
    else:
        arr[i] = -1
      
for i in range(26):
    print(arr[i],sep= " ", end = " ")