# #10816 숫자카드 2
# import sys
# import bisect

# n = int(input())
# card = list(map(int,sys.stdin.readline().split()))
# m = int(input())
# li = list(map(int,sys.stdin.readline().split()))
# tmp = li.copy()

# answer = []

# def binary_search(num, li = []):
#     li.sort()
#     mid = len(li) // 2
#     min = 0
#     max = len(li) - 1
#     while min <= max:
#         mid = (max + min) // 2 
#         if li[mid] == num:
#             return num
#         elif li[mid] <= num:
#             min = mid + 1
#         else:
#             max = mid - 1
    
# for i in card:
#     if bisect.bisect_left(tmp,i) == None:
#         continue
#     else:
#         answer.append(i)

# for i in range(len(tmp)):
#     li[i] = answer.count(li[i])
#     #print(li[i],end=" ")

# print(li)
import bisect 
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))
card.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect.bisect_right(a, right_value)
    left_index = bisect.bisect_left(a, left_value)
    return right_index - left_index


for i in range(len(test)):
    print(count_by_range(card, test[i], test[i]), end=' ')