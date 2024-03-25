n = int(input())
li = list(map(int,input().split()))

m = int(input())
arr = list(map(int,input().split()))

li.sort()

def binaryserach(lis,target,start,end):
    if start > end:
        return None
    
    mid = (start+end) // 2
    
    if lis[mid] == target:
        return mid
    
    elif lis[mid] < target:
        return binaryserach(lis,target,mid + 1,end)
    else:
        return binaryserach(lis,target,start,mid - 1)

answer = []

for i in arr:
    if binaryserach(li,i,0,len(li) - 1) == None:
        answer.append("no")
    else:
        answer.append("yes")
        
print(answer)