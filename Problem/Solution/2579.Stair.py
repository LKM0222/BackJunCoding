#2579 계단오르기
n = int(input())
s = [0] + list(int(input()) for i in range(n))
dp = [0] * 301

if n == 1:
    print(s[1])
elif n == 2:
    print(s[2] + s[1])
else:
    dp[1] = s[1]
    dp[2] = s[1] + s[2]
    dp[3] = max(s[1] + s[3] , s[2] + s[3])
    for i in range(4,n+1):
        dp[i] = max(dp[i - 3] + s[i-1] + s[i], dp[i - 2] + s[i])

    print(dp[n])