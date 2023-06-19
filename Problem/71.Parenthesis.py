#9012
n = int(input())

for _ in range(n):
    stack = []
    s = input()
    for i in s:
        if i == '(': #여는괄호일경우
            stack.append('(')
        
        else: #닫는 괄호일 경우
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    
    else:
        if not stack:
            print("YES")
        else:
            print("NO")

    