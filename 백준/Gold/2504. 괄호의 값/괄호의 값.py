

def check_e (e):
    
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(e)):
        
        if e[i] == '(':
            temp *= 2
            stack.append('(')
        elif e[i] == '[':
            temp *= 3
            stack.append('[')
        elif e[i] == ')':
            if not stack or stack[-1] != '(':
                return 0
            if e[i-1] =='(':
                result += temp
            stack.pop()
            temp//=2
        elif e[i] == ']':
            if not stack or stack[-1] != '[':
                return 0
            if e[i-1] == '[':
                result += temp
            stack.pop()
            temp//=3
    return result if not stack else 0

ex = input().strip()
print(check_e(ex))
# print()