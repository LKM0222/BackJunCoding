#2784 피보나치수2

n = int(input())

fibo_arr = [0] * (n+1)

fibo_arr[0] = 0

fibo_arr[1] = 1

for n in range(2,n+1):
    fibo_arr[n] = fibo_arr[n-1] + fibo_arr[n-2]
    
print(fibo_arr[n])