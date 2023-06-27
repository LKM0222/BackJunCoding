#3052 나머지
li = []

for i in range(10):
    li.append(int(input()))

temp = []
for i in li:
    try:
        n = i % 42
        if temp.index(n):
            continue

    except ValueError:
        temp.append(n)
    
print(len(temp))
