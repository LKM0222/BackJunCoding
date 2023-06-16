#15829 Hashing

L = int(input())
s = input()
t = 0
for i in range(len(s)):
    n = ord(s[i]) - 96
    t += n * (31 ** i)

print(t % 1234567891)