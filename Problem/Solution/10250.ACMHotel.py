#10250 ACM 호텔

a = int(input())
for i in range(a):
    h,w,n = map(int,input().split())
    m = n % h #floor
    if m == 0: 
        print(h * 100 + n // h)
    else:
        print(m * 100 + n// h + 1)