#1149 RGB거리 (다이나믹프로그래밍)
import sys

n = int(sys.stdin.readline())
dp = [0] * n

for i in range(n): #입력 받기
    x,y,z = map(int, sys.stdin.readline().split())
    
    now = [0,0,0]
    
    if i == 0:
        dp[0] = [x,y,z]
    
    else:
        #더하기
        if dp[i-1][1] + x < dp[i-1][2] + x: #작은 값을 찾아서 저장
            now[0] = dp[i-1][1] + x
        else:
            now[0] = dp[i-1][2] + x
            
        if dp[i-1][0] + y < dp[i-1][2] + y:
            now[1] = dp[i-1][0] + y
        else:
            now[1] = dp[i-1][2] + y
            
        if dp[i-1][0] + z < dp[i-1][1] + z:
            now[2] = dp[i-1][0] + z
        else:
            now[2] = dp[i-1][1] + z
            
        dp[i] = now
    
        
print(min(dp[n-1]))