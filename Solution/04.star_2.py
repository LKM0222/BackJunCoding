#2439
n = int(input())

for i in range(n):
    i += 1
    print(" " * (n-i) + "*" * i) #문자열이 두개니깐 그냥 + 연산으로 이어도 됨. 굳이 , 를 사용할 필요는 없음...!