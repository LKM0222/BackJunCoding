from collections import deque

def solution(rows, columns, queries):
    answer = []
    
    #2차원 배열 선언
    arr = [[0 for j in range(columns)] for i in range(rows)]
    x = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = x
            x += 1
    
    #값 저장위한 배열
    temp = []
    
    #돌리기
    for temp in queries:
        #기준점
        x1,y1 = temp[0] - 1, temp[1] - 1
        x2,y2 = temp[2] - 1, temp[3] - 1
        
        print("x1,y1",x1,y1, " x2,y2 " ,x2,y2)
        print(x2-x1)
        #큐에 순서대로 넣기
        queue= deque()
        
        #왼쪽
        for i in range(x2-x1):
            queue.append(arr[y1][x1+i])
        #아래
        for i in range(y2-y1):
            queue.append(arr[x2][y1+i])
        #오른쪽
        for i in range(x2 - x1):
            queue.append(arr[y1][x2-i])
        #위
        for i in range(y2 - y1):
            queue.append(arr[y2-i][x2])
        
        print(queue)
        
            

    return answer

print(solution(6,6,[[2,2,5,4]]))