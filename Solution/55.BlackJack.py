#2798 블랙잭

n, m = map(int,input().split())

s = list(map(int,input().split(' ')))
minn = 0
arr = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            x = s[i] + s[j] + s[k]
            if x <= m and x >= minn:
                minn = x

print(minn)