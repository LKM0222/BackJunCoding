#10816 숫자카드 2
import sys

n = int(input())
card = list(map(int,sys.stdin.readline().split()))
m = int(input())
li = list(map(int,sys.stdin.readline().split()))
tmp = li
li.sort()

answer = []

def binary_search(num, li = []):
    mid = len(li) // 2
    min = 0
    max = len(li) - 1
    while min <= max:
        mid = (max + min) // 2 
        print(max,min,mid)
        if li[mid] == num:
            return num
        elif li[mid] <= num:
            print(min,"min")
            min = mid + 1
        else:
            max = mid - 1
    
        
    


for i in li:
    if binary_search(i,card) == None:
    
