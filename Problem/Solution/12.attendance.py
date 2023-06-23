#5597 과제 안내신분..?

li = []
for i in range(28):
    li.append(int(input()))

for i in range(1,31):
    try:
        if li.index(i):
            continue

    except ValueError:
        print(i)