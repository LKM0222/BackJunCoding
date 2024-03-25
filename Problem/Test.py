li = [0,2,4,6,8,10,12,14,16,18,20]

#재귀적

def binary(array,target,start,end):
    mid = (start + end) // 2 #몫만 취한다  
    if start > end:
        return None #못찾았다면 None반환
    
    if array[mid] == target:
        return mid #찾았다면 인덱스 반환
    elif array[mid] < target:
        return binary(array,target, mid + 1, end) #찾는값보다 중간값이 작다면 mid아래쪽을 버림
    else:
    	return binary(array,target, start, mid - 1) #크다면, mid위쪽을 버림.
        
binary(li,7,0,len(li) - 1)    
    
    
 
#반복적

start = 0
end = len(li) - 1 #인덱스니깐 1 빼줌

target = 7

while start <= end:
    mid = (start + end) // 2
    
    if li[mid] == target:
        break #찾았다면 바로 반복문 탈출. mid의 변경 없음.
    elif li[mid] < target:
        start = mid + 1 
    else:
        end = mid - 1
        
print(li[mid])