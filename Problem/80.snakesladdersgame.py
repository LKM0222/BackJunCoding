#16928 뱀과 사다리 게임
import sys
l,s = map(int,input().split())

snake = []
ladder = []
moveflag = False

for i in range(l):
    ladder.append(list(map(int,sys.stdin.readline().split())))

for i in range(s):
    snake.append(list(map(int,sys.stdin.readline().split())))

snake.sort(key= lambda x:x[0])
ladder.sort(key= lambda x:x[0])

c = 0
nowPos = 1


nextLadderPos = []
nextSnakePos= []

def FindLadderPos(num,now):
    #print("findladderPos...")
    for i in ladder:
        if i[0] <= num and now <= i[0]:
            nextLadderPos.append(i)
    
    #print(nextLadderPos)

def FindSnakePos(num,now):
    #print("findSnakePos...")
    for i in snake:
        if i[0] <= num and now <= i[0]:
            nextSnakePos.append(i)
    
    #print(nextSnakePos)


while nowPos <= 100:
    # print("nowpos:",nowPos)
    c += 1
    # print("count:",c)
    
    nextPos = nowPos + 6 #최대로 갈 수 있는 위치

    #사다리의 위치를 찾아야됨
    FindLadderPos(nextPos,nowPos)
    #뱀의 위치도 찾아야됨.
    FindSnakePos(nextPos,nowPos)

    if len(nextLadderPos) == 0 and len(nextSnakePos) == 0:
        # print("ladder, snake not found")
        nowPos += 6 #찾은 사다리와 찾은 뱀이 아무것도 없다면 그냥 최대로 움직인다.
        continue
    
    else:
        if len(nextLadderPos) > 0 : 
            maxLadder = max(nextLadderPos,key = lambda x: x[1])
            # print("maxLadder:",maxLadder)
        if len(nextSnakePos) > 0 : 
            minSnake = min(nextSnakePos, key = lambda x:x[1])
            # print("minSnake:",minSnake)


    #움직일 수 있는 칸 조회 시작
    for i in range(6,0,-1):
        if moveflag:
            # print("moveComplete")
            break
        
        temp = nowPos + i
        # print("move Start!",temp,nowPos)
        
        
        if len(nextSnakePos) == 6:#갈 수 있는 모든칸이 뱀이라면
            # print("can move all snake")
            #뱀 중 가장 작은 위치로 바꾼다.
            nowPos = minSnake
            moveflag = True
                
        else:
            #사다리부터 조회
            for j in nextLadderPos:
                if temp == j[0]:
                    # print("find ladder!",j)
                    if j[1] == maxLadder[1]:
                        # print("it's max ladder!")
                        nowPos = j[1]
                        moveflag = True
                    # else:
                        # print("but it's not max ladder...")

            #찾은 뱀의 위치를 조회
            for j in nextSnakePos:
                if temp == j[0]:#그 해당 칸에서 뱀을 만났다면,
                    # print("it's snake",j)
                    break#그 위치는 갈 수 없다.
                else: #만나지 않았다면
                    nowPos = temp #temp만큼 움직이고
                    moveflag = True #움직였다고 표시
                    break
            
            
            
            

    moveflag = False
    nextLadderPos.clear()
    nextSnakePos.clear()

print(c)



    