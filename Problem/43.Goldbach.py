#9020 골드바흐의 추측

def Prime(n):
    if n == 1: return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0: return False
    
    return True

li = list(range(1,10000))
arr = []
for i in li:
    if Prime(i): arr.append(i)


n = int(input())

for i in range(n):
    x = int(input())
    tmp = []
    diff = []
    for a in arr:
        for b in arr:
            if b > x:
                break

            if a + b == x:
                tmp.append([a,b])
                diff.append(a-b)
            
        if a > x: break

    for i in range(len(diff)):
        if diff[i] == 0:
            t = tmp[i]
            print(t[0],t[1])
            break
        if diff[i] > 0:
            t = tmp[i - 1]
            print(t[0],t[1])
            break
