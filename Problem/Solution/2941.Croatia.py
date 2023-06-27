#2941 크로아티아 알파벳 
#c= c- dz= d- lj nj s= z=
#cli = "č ć dž đ lj nj š ž".split()
#크로아티아 문자를 아에 삭제시키는게 아니라 다른 문자 하나로 (특수문자 여기서는 띄어쓰기) 바꾸고 전체 길이를 출력하면 됨.
li = "c= c- dz= d- lj nj s= z=".split()
count = 0

s = str(input())
for i in li:
    if i in s:
        s = s.replace(i,' ')

print(len(s))