n = int(input())

li = []

for i in range(n):
    x,y = input().split()
    li.append((x,int(y)))

def score(data):
    return data[1]
    
li.sort(key = score)

for i in li:
    print(i[0])
    
    
#람다함수를 쓰면 다음과 같이 쓰면 됨

li.sort(key = lambda x : x[1])