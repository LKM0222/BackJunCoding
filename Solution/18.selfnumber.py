#4673 셀프넘버

def selfnum(d) -> int:
    s = str(d)
    t = d
    for i in s:
        t += int(i)
    return t

gen = [] #생성자가 있는 수들

for i in range(10001):
    gen.append(selfnum(i))

gen.sort()
for i in range(10001):
    if i in gen:
        continue
    else:
        print(i)