#1620 나는야 포켓몬 마스터 이다솜
import sys

n ,m= map(int,input().split())
by_id={}
by_name={}
for i in range(1,n+1):
    st = sys.stdin.readline().rstrip()
    by_id[i] = st
    by_name[st] = i

for i in range(m):
    st = sys.stdin.readline().rstrip()
    if st.isdigit():
        print(by_id[int(st)])
    else:
        print(by_name[st])