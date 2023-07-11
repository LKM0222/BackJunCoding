#17219  비밀번호 찾기
import sys
password = {}

n ,m = map(int,input().split())
for i in range(n):
    s = sys.stdin.readline().split()
    password.update()
    password[s[0]] = s[1]
    

for i in range(m):
    s = sys.stdin.readline().rstrip()
    print(password[s])