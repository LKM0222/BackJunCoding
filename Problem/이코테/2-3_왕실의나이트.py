s = input()

n = str(ord(s[0]) - 96) + s[1]

#8방향만 조사하면 됨

x,y = int(n[0]), int(n[1])
#print(x,y)

count = 0

if x - 2 > 0: #왼쪽 이동 가능
    if y - 1 > 0: #위 이동 가능
        #print("10")
        count += 1
    if y + 1 < 9:#아래 이동 가능
        #print("8")
        count += 1
    
if x + 2 < 9: #오른쪽 이동 가능
    if y - 1 > 0: #위 이동 가능
        #print("2")
        count += 1
    if y + 1 < 9:#아래 이동 가능
        #print("4")
        count += 1

if y - 2 > 0: #위 이동 가능
    if x - 1 > 0: #왼쪽 이동 가능
        #print("11")
        count += 1
    if x + 1 < 9: #오른쪽 이동 가능
        #print("1")
        count += 1

if y + 2 < 9: #아래 이동 가능
    if x - 1 > 0: #왼쪽 이동 가능
        #print("7")
        count += 1
    if x + 1 < 9: #오른쪽 이동 가능
        #print("5")
        count += 1
            
print(count)
        

# #정석 정답
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     #이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)